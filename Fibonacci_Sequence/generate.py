#!/usr/bin/env python
# Script to generate the nth Fibonacci term (https://thecodeaddict.wordpress.com/2012/01/03/fibonacci-sequence-part-2/)

from math import sqrt

#Iterative method
def F_iter(n) :
    if n == 0 or n == 1: return n
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, (a + b)
    return b

#Recursive method
def F_rec(n) :
    if n == 0: return 0
    elif n == 1: return 1
    return F_rec(n-1) + F_rec(n-2)

#Golden ratio method
def F_phi(n) :
	phi = (1+sqrt(5))/2
	ans = round((phi**n)/sqrt(5))
	if n < 0: ans = (-1)**(n+1) * ans
	return ans

def main():
	term = int(input("Enter the number of Fibonacci terms to display: "))	
	method = int(input("Choose a method of generating the terms:\n\t[1] Iterative\n\t[2] Recursive\n\t[3] Golden ratio\n-> "))
	if method == 1:
		print(list(map(F_iter, range(0,term))))
	elif method == 2:
		print(list(map(F_rec, range(0,term))))
	elif method == 3:
		print(list(map(F_phi, range(0,term))))

if __name__ == "__main__": main()