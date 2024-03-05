#  7. Create a generator method to have the prime numbers using yield between 1 and 100.

def generate_primes():
    primes = []
    candidate = 2

    while candidate <= 100:
        is_prime = all(candidate % prime != 0 for prime in primes)
        if is_prime:
            primes.append(candidate)
            yield candidate
        candidate += 1


list(map(lambda x: print(x), generate_primes()))
