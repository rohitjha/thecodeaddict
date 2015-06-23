#!/usr/bin/env python
#!Script to recognize Fibonacci terms and to determine index of these terms (https://thecodeaddict.wordpress.com/2012/01/03/fibonacci-sequence-part-2/)

def isPerfectSquare1(n) :
    a = sqrt(n)
    return a % 1 == 0

def isPerfectSquare2(n) :
    a = int(sqrt(n))
    return a*a == n

def isPerfectSquare3(n) :
    if n < 0: return False
    if (n & 0xF) in (0, 1, 4, 9) : return sqrt(n)%1 == 0
    return False

def isFibTerm(n) :
    a = 5*n*n
    x, y = a + 4, a - 4
    return isPerfectSquare3(x) or isPerfectSquare3(y)

def fibIndex(n) :
    if isFibTerm(n) :
        phi = (1 + sqrt(5)) / 2
    return int(ceil((log10(n) + log10(5)/2) / log10(phi)))