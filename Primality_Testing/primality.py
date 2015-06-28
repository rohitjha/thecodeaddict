#!/usr/bin/env python
# Python functions for primality testing (https://thecodeaddict.wordpress.com/2011/10/29/primality-testing/)

def is_prime1(n) :
    for m in range(2, n) :
        if n % m == 0: return False
    return True

def is_prime2(n) :
    for m in range(2, int(sqrt(n))+1) :
        if n % m == 0: return False
    return True

def is_prime3(n) :
    if n == 2: return True
    if n % 2 == 0: return False
    for m in range(3, int(sqrt(n))+1, 2) :
        if n % m == 0: return False
    return True

def is_prime4(n) :
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
 
    sqrtN = int(sqrt(n))+1
    for i in range(6, sqrtN) :
        if n%(i-1) == 0 or n%(i+1) == 0: return False
    return True

def is_prime5(n) :
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
 
    r, f = int(sqrt(n)), 5
 
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0: return False
        f += 6
    return True