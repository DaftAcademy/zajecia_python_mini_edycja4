import os

from file_hasher import get_hash


def duplicate_finder(topdir=None):
    if topdir is None:
        topdir = os.getcwd()
    data = {}
    hashed_files = set()
    hashes = {}
    for root, dirs, files in os.walk(topdir):
        #print(root, dirs, files)
        for single_file in files:
            f_path = os.path.join(root, single_file)
            size = os.path.getsize(f_path)
            size_list = data.get(size, [])
            size_list.append(f_path)
            if len(size_list) > 1:
                for file_path in size_list:
                    if file_path not in hashed_files:
                        f_hash = get_hash(file_path)
                        size_hash_list = hashes.get(f_hash, [])
                        size_hash_list.append(file_path)
                        hashes[f_hash] = size_hash_list
                        if len(size_hash_list) > 1:
                            print(
                                'hash {} collision for following files:\n\t{}\n'.format(
                                    f_hash, '\n\t'.join(size_hash_list)
                                )
                            )
            data[size] = size_list
    # TODO: PRACA DOMOWA: w tym miejscu porównać binarnie pliki, ponieważ
    # identyczne wartości hash nie znaczą, że pliki są identyczne
    # podpowiedź: https://docs.python.org/3.5/library/filecmp.html
    return data, hashes
    
def format_dict(my_dict):
    keys = list(my_dict.keys())
    keys.sort()
    entry_format = '\t{}: {}'
    entry_lines = (entry_format.format(k, my_dict[k]) for k in keys)
    return '{}\n{}\n{}'.format('{', '\n'.join(entry_lines), '}')
        
        
data, hashes = duplicate_finder()
print(format_dict(data))
print(format_dict(hashes))
