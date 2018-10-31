#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 01:05:20 2018

@author: rocia
"""

def isPrime(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True

def compute(limit):
    sumOprimes = 0
    for x in range(2,limit+1):
        if isPrime(x):
            sumOprimes += x
    return sumOprimes
            

print(compute(2000000))