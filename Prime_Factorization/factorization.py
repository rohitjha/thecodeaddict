#!/usr/bin/env python
#Script for generating prime factors of a number (https://thecodeaddict.wordpress.com/2012/02/26/prime-factorization/)

from math import sqrt

def prime_sieve(limit) :
    crosslimit = int(sqrt(limit))
    sieve = [False]*limit

    for n in range(4, limit, 2) :
        sieve[n] = True
    for n in range(3, crosslimit+1, 2) :
        if not sieve[n]:
            for m in range(n*n, limit, 2*n) :
                sieve[m] = True

    num_primes = 0
    primes = []
    for n in range(2, limit) :
        if not sieve[n]:
            num_primes += 1

    for n in range(2, limit) :
        if not sieve[n]:
            primes.append(n)

    return primes


def trial_division(n) :
    if n == 1: return [1]
    primes = prime_sieve(int(n**0.5) + 1)
    prime_factors = []

    for p in primes:
        if p*p > n: break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1: prime_factors.append(n)

    return prime_factors


def main():
    num = int(input("Enter a number to be factorized: "))
    print("Its factors are: " + str(trial_division(num)))

if __name__ == "__main__": main()