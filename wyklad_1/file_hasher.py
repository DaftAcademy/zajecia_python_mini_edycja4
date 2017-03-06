import hashlib
# https://en.wikipedia.org/wiki/Pigeonhole_principle
# https://pl.wikipedia.org/wiki/Zasada_szufladkowa_Dirichleta


def get_hash(f_path, mode='md5'):
    h = hashlib.new(mode)
    # TODO: PRACA DOMOWA: Nie czytać całego pliku na raz tylko po kawałku
    f = open(f_path, 'rb') # otwiera plik w funkcji hashującej, co z obsługą błedów?
    h.update(f.read()) # czyta cały plik na raz!
    hash_text = h.hexdigest()
    f.close()
    return hash_text
    
#print(get_hash('plik_testowy'))
#print(get_hash('sha1_collisions/shattered-1.pdf', mode='sha1'))
#print(get_hash('sha1_collisions/shattered-2.pdf', mode='sha1'))

# eb63071881718ed66bb75ce670e65b9e
# eb63071881718ed66bb75ce670e65b9e

