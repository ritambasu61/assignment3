#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 00:1:59 2019

@author:ritambasu61
"""

import numpy as np
def g(z):
    return np.exp(z)
x=np.arange(0,1,.001)
y=g(x)
print('Integration of exp(x) from x=0 to x=1 (by trapezoidal Method) is =:',np.trapz(y,x))
