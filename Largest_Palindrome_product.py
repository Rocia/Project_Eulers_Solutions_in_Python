#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 01:47:48 2018

@author: rocia
"""
def isPalindrome(n):
    lst, b = list(map(int, str(n))), list(map(int, str(n)))
    b.reverse()
    if lst == b:
        return True
    else:
        return False
    
def make_Nos(N):
    num = ""
    while N != 0:
        num = num + '9'
        N -= 1
    num = int(num)
    return (num, num)
    
def find_largest_palindrome(N):
    Pals, Res = [],{}
    a, b = make_Nos(N)
    for i in range(a,1,-1):
        for j in range (b,1,-1):
            if isPalindrome(i*j):
                Pals.append(i*j)
                Res[i*j] = (i,j)
                break
    Pal = max(Pals)
    return (Pal)
if __name__ == "__main__":
    N = 3
    #N = int(input("Enter the number of Digits"))
    pal = find_largest_palindrome(N)
    #n1, n2, pal = find_largest_palindrome(N)
    print ('The largest Palindrome in a',N,'digit number is',pal)#'which is the product of',n1,'and',n2)
