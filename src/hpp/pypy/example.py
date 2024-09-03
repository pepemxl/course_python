# primes.py

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(limit):
    count = 0
    for i in range(limit):
        if is_prime(i):
            count += 1
    return count

if __name__ == "__main__":
    limit = 100000
    print(f"Number of primes up to {limit}: {count_primes(limit)}")
