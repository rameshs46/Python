#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program No: 8
Created on Mon May 16 22:35:48 2022
Description: Print the digit of a three digit number
@author: rameshsengamalai
"""
n =int(input('Enter three digit integer number: '))
p = n%10
q = n//10
r = q%10
s = q//10
print(p)
print(r)
print(s)
