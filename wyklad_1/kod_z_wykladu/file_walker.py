import os
from pprint import pprint

def my_dir_walker_with_size_counting(topdir=None):
    if topdir is None:
        topdir = os.getcwd()
    sizes = {topdir: 0} # ścieżka: rozmiar w bajtach
    stack = []
    
    def inner_walker(new_topdir):
        stack.append(new_topdir)
        new_topdir_size = os.path.join(*stack)
        entries = os.scandir(new_topdir)
        size = 0
        for entry in entries:
            if entry.is_dir(follow_symlinks=False):
                entry_size = inner_walker(entry.name)
                sizes[os.path.join(*stack)] = entry_size
                size += entry_size
                stack.pop()
            else:
                fpath = os.path.join(*stack, entry.name)
                sizes[fpath] = os.path.getsize(fpath)
                size += os.path.getsize(fpath)
        return size
    inner_walker(topdir)
    return sizes
        
pprint(my_dir_walker_with_size_counting('/home/marcin'))
