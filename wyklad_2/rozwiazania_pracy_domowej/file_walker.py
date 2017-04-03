import logging
import os


def sample_directory_walker(new_cwd=None):
    old_cwd = os.getcwd()
    if new_cwd:
        os.chdir(new_cwd)
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        print('{}, {}, {}\n'.format(root, dirs, files))
    if new_cwd:
        os.chdir(old_cwd)


def format_sizes(sizes):
    keys = list(sizes.keys())
    keys.sort()
    entry_format = '\t{}: {}'
    entry_lines = (entry_format.format(k, sizes[k]) for k in keys)
    return '{}\n{}\n{}'.format('{', '\n'.join(entry_lines), '}')


def my_directory_walker_with_size_counting(topdir=None):
    if topdir is None:
        topdir = os.getcwd()
    sizes = {topdir: 0}
    root_stack = []

    def inner_walker(new_topdir):
        root_stack.append(new_topdir)
        new_topdir_path = os.path.join(*root_stack)
        try:
            entries = os.scandir(new_topdir_path)
        except Exception:
            logging.warning(
                'Got I/O error while scanning path, skipping {}.'.format(
                    new_topdir_path
                )
            )
            return 0

        size = 0
        for entry in entries:
            if entry.is_dir(follow_symlinks=False):
                entry_size = inner_walker(entry.name)
                sizes[os.path.join(*root_stack)] = entry_size
                size += entry_size
                root_stack.pop()
            elif entry.is_file(follow_symlinks=False):
                sizes[os.path.join(*root_stack, entry.name)] = (
                    entry.stat().st_size
                )
                size += entry.stat().st_size
        return size

    sizes[topdir] = inner_walker(topdir)
    return sizes
