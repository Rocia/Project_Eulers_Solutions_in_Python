#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 02:36:11 2018

@author: rocia
"""
def get_range():
    a = int(input("Enter Start of Range"))
    b = int(input("Enter End of Range"))
    if b>a:
        return (a,b)
    else:
        print('Invalid Range! Enter Valid Range')
        get_range()
    
def compute_sdn():
    num, Cntinu = 1, True
    a, b = get_range()
    while Cntinu:
        for n in range (a,b+1):
            if num % n != 0:
                num += 1
                break
            if num % n == 0 and n == b:
                Cntinu = False
    return num

if __name__ == "__main__":
    print(compute_sdn())
        
        
    