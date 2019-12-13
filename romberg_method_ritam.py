#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 00:10:49 2019

@author:ritambasu61
"""

from scipy import integrate
import numpy as np
def f(x):
    return np.exp(x)
print('Integration of exp(x) from x=0 to x=1 (by Romberg Quadrature Method) is =:',integrate.romberg(f,0,1))
