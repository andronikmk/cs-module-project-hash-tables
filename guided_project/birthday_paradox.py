# make a bunch of random keys
# bash them
# track the as we go
# stop when we get a collison
import random
import hashlib

def hash_func(key):
    return int(hashlib.sha256(f'{key}'.encode()).hexdigest(), 16)

def how_many_before_sollision(array_size):
    previous_key = set()
    successful_hashes = 0
    while True:
        random_key = random.random()
        hashed_key = hash_func(random_key) % array_size

        if hashed_key not in previous_key:
            previous_key.add(hashed_key)
            successful_hashes += 1
        else: # collision
            break

    print(f"buckets: {array_size}, tries {successful_hashes} before collison, {successful_hashes/array_size * 100} percent full")

how_many_before_sollision(8)
how_many_before_sollision(16)
how_many_before_sollision(32)
how_many_before_sollision(64)
how_many_before_sollision(128)
how_many_before_sollision(256)
how_many_before_sollision(512)
how_many_before_sollision(1024)
how_many_before_sollision(2048)

