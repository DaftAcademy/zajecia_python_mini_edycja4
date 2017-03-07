import hashlib 

def get_hash(f_path, mode='md5'):
    h = hashlib.new(mode)
    f = open(f_path, 'rb')
    h.update(f.read())
    hash_text = h.hexdigest()
    # 'eb63071881718ed66bb75ce670e65b9e'
    f.close()
    return hash_text
    
if __name__ == '__main__':
    #print(get_hash('/home/marcin/kursy/MINI_4/wyklad_1/plik_testowy', 'sha1'))
    #38762cf7f55934b34d179ae6a4c80cadccbb7f0a
    print(get_hash('/home/marcin/kursy/MINI_4/wyklad_1/sha1_collisions/shattered-1.pdf', 'sha1'))
    print(get_hash('/home/marcin/kursy/MINI_4/wyklad_1/sha1_collisions/shattered-2.pdf', 'sha1'))
