#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 01:50:26 2018

@author: rocia
"""
def factors(x):
   fctrs = []

   for i in range(1, x + 1):
       if x % i == 0:
           fctrs.append(i)
           
   return fctrs



def compute(D):
    Case = True
    limit= 1
    while Case:
        Num = sum(x for x in range(limit+1))
#        print(Num)
        l = len(factors(Num))
        print(l)
        if l >= D:
            Case = False
            return Num
        else:
            limit += 1


print(compute(50))