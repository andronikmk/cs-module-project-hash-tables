cache = {}
def fib(n):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

print(fib(50))
