"""find the factors in 100"""

def factors(num):
    """Create a traditional function that finds all factors of an integer and stores them in a list."""
    results = []
    for k in range(1, num+1):
        if num % k == 0:
            results.append(k)
    return results

example = factors(100)
print(example)

def factors_generator(num):
    """Create a generator for finding all factors of an integer."""
    for k in range(1, num+1):
        if num % k == 0:
            yield k

example2 = factors_generator(100)
print(example2)