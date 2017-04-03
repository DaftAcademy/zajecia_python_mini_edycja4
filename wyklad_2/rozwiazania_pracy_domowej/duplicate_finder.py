import filecmp
import os

from file_hasher import get_hash


def duplicate_finder(topdir=None):
    if topdir is None:
        topdir = os.getcwd()

    data = {}  # rozmiar_pliku: lista plików o tym rozmiarze
    hashed_files = set()
    hashes = {}  # hash: lista plików o tym samym hashu
    for root, dirs, files in os.walk(topdir):
        for single_file in files:
            f_path = os.path.join(root, single_file)
            size = os.path.getsize(f_path)
            size_list = data.get(size, [])
            size_list.append(f_path)
            data[size] = size_list
            if len(size_list) > 1:
                for file_path in size_list:
                    if file_path not in hashed_files:
                        f_hash = get_hash(file_path, 'sha1')
                        hash_list = hashes.get(f_hash, [])
                        hash_list.append(file_path)
                        hashes[f_hash] = hash_list
                        hashed_files.add(file_path)

    grouped_files = {}
    for hash_value, files in hashes.items():
        grouped_files[hash_value] = []
        for file in files:
            group_found = False

            for group in grouped_files[hash_value]:
                any_file_from_set = next(iter(group))
                if filecmp.cmp(file, any_file_from_set, shallow=False):
                    group.add(file)
                    group_found = True
                    break

            if not group_found:
                grouped_files[hash_value].append({file})

    duplicates = {}
    for hash_value, grouped_files in grouped_files.items():
        duplicates[hash_value] = [
            group for group in grouped_files if len(group) > 1
        ]

    return duplicates

