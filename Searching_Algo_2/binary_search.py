#!/usr/bin/env python
# Script for binary search (https://thecodeaddict.wordpress.com/2011/11/17/searching-algorithms-part-2/)

# Iterative Binary Search
def iter_bs(a, value) :
    low, high = 0, len(a)-1
    while low <= high:
        mid = (low + high)//2
        if value == a[mid]:
            return "The element %s was found at index %s" % (value, mid)
        if value < a[mid]:
            high = mid - 1
        else:
        	low = mid + 1
 
    return "The element %s was not found." % value

# Recursive Binary Search
def rec_bs(a, value, low, high) :
    if high < low:
        return "The element %s was not found." % value
    mid = low + (high - low)//2
    if a[mid] > value:
        return rec_bs(a, value, low, mid-1)
    elif a[mid] < value:
        return rec_bs(a, value, mid+1, high)
    
    return "The element %s was found at index %s." % (value, mid)