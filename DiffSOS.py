#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 04:00:17 2018

@author: rocia
"""

def sumOsqr(n):
    sum = 0
    for i in range(1,n):
        sum = sum + i*i
    return sum

def sqrOsum(n):
    sum = 0
    for i in range(1,n):
        sum = sum + i
    return sum*sum

def diff(n):
    sos , sqos = sumOsqr(n) , sqrOsum(n)
    print(sqos, sos)
    return sqos - sos

if __name__ == "__main__":
    N= 100

    #N = int(input("Enter a no."))
    print(diff(N))