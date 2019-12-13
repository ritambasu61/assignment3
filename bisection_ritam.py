#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  10 19:59:38 2019

@author:ritambasu61
"""
from scipy import optimize
from numpy import sin,cos,exp
def f(x):
    return sin(cos(exp(x)))
r=optimize.bisect(f,-1,1)#calculating the root
print ('root is',r)
print ('value of f(x) at the root is',f(r))