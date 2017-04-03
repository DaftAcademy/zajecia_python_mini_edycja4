import hashlib
import logging


CHUNK_SIZE = 8192


def get_hash(f_path, mode='md5'):
    h = hashlib.new(mode)
    try:
        with open(f_path, 'rb') as f:
            buff = f.read(CHUNK_SIZE)
            while buff:
                h.update(buff)
                buff = f.read(CHUNK_SIZE)
            return h.hexdigest()
    except OSError as e:
        logging.warning(
            'Got an error during file {} opening. '
            'Error: {}'.format(f_path, e)
        )
