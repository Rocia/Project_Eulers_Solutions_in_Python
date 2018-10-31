#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 04:22:37 2018

@author: rocia
"""

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def compute(n):
    lst, i, Cntinu = [], 1, True
    while Cntinu:
        i += 1
        if isPrime(i):
            lst.append(i)
        if len(lst) == n:
            Cntinu = False
    return lst[-1]

print(compute(10001))


             