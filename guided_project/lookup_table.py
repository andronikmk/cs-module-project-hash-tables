import math

lookup_table = {}

def inverse_root(n):
    return 1 / math.sqrt(n)

def build_lookup_table():
    for i in range(1, 1000):
        lookup_table[i] = inverse_root(i)

build_lookup_table()

print(lookup_table[10])
