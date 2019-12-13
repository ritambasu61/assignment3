#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  10 20:10:36 2019

@author:ritambasu61
"""

from scipy import optimize
from numpy import sin,cos,exp
def f(x):
    return sin(cos(exp(x)))

def derf(x):  # derivative of the given function
    return -cos(cos(exp(x)))*cos(exp(x))*exp(x)
r1=optimize.newton(f,-1,derf)
print ('root with initial guess x=-1 is',r1) 
r2=optimize.newton(f,-0.1,derf)
print ('root with initial guess x=-1 is',r2)
