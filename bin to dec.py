# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:00:29 2019

@author: Abhijeet
"""

"""binary to decimal"""
def dec(n):
    
    a=str(n)
    l=len(a)
    p=0
    d=0
    for i in range(-1,-l-1,-1):
        x=int(a[i])*(2**p)
        p+=1
        d+=x
    return(d)    
n=int(input("number in binary form: "))
print("decimal number is: ",dec(n))
"""decimal to binary"""
def b(x):
     t=0
     s=0
     while x!=0:
          a=x%2
          s=s+(a*10**t)
          t+=1
          x=x//2
     print(s)
n=int(input("number in decimal form:  "))
b(n)

