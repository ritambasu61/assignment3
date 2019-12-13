#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 00:11:40 2019

@author:ritambasu61
"""

from scipy import integrate
import numpy as np
def f(x):
    return np.exp(x)
print('Integration of exp(x) from x=0 to x=1 (5th oder Fixed-Quadrature Method) is =:',integrate.fixed_quad(f,0.0,1.0,n=5))
