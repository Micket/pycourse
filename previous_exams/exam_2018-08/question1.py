from collections import defaultdict
import hashlib

def read_checksums(filename):
    filedb = defaultdict(dict)
    with open(filename) as f:
        for line in f:
            path, hashes = line[1:].split('"')
            for h in hashes.strip().split():
                hash_type, hash_hex = h.split(':')
                filedb[path][hash_type.strip()] = hash_hex.strip()
    return filedb


def verify_files(hashdb):
    for path, hashes in hashdb.items():
        try:
            with open(path, 'rb') as f:
                data = f.read()
        except FileNotFoundError:
            print('Error! "{}" missing'.format(path))
            continue

        for hash_type, hash_hex in hashes.items():
            hasher = hashlib.new(hash_type)
            hasher.update(data)
            verify = hasher.hexdigest()
            if verify != hash_hex:
                print('Error! "{}" differs from {}:{} ({})'.format(path, hash_type, hash_hex, verify))

hashdb = read_checksums('checksums.txt')
verify_files(hashdb)
