#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 00:06:54 2018

@author: rocia
"""

def pythog_triplets(N):
    for x in range(1,N):
        for y in range(x+1,N):
            z = y + 1
            while z * z < x * x + y * y :
                z = z + 1
                if z * z == x * x + y * y and z <= N and x+y+z == N:
                    return x,y,z
 
        
if __name__ == "__main__":
    a, b, c = pythog_triplets(1000)
    print(a,b,c)