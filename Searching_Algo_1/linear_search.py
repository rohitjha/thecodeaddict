#!/usr/bin/env python
# Python script for linear search

# Returns index of the value, if found. Otherwise returns False.
def FOR_search(a_list, value, start = 0) :
    found = False
    l = len(a_list)
    if l == 0: return "List is empty."
 
    for index in range(start, l) :
        if a_list[index] == value:
            found = True
            return index
 
    if not found:
        return "%s was not found in the list." % value

# Returns True if found, otherwise False.
def REC_search(a_list, value) :
    if len(a_list) != 0:
        if a_list[0] == value:
            return True
        else:
            a_list = a_list[1:]
            return REC_search(a_list, value)
 
    else: return False

# Returns last index of value if found. Otherwise returns False.
def REV_search(a_list, value) :
    i = len(a_list) - 1
    while i >= 0:
        if a_list[i] == value:
            return i
        i = i-1
    return False

# Return index of value.
def SEN_search(a_list, value) :
    a_list.append(value)
    index = 0
 
    while True:
        if a_list[index] == value: break
        index = index+1
    return index

# Return True or False.
def ORD_search(a_list, value) :
    index = 0
    while True:
        assert index < len(a_list)
        if a_list[index] == value: return True
        elif a_list[index] > value: return False
        index = index+1
    return False