#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  10 19:32:54 2019

@author:ritambasu61
"""

from matplotlib import pyplot as plt
import numpy as np
import scipy.interpolate as sci
x=[0,1,2,3,4,5]      # Given Data 
y=[1.0,2.0,1.0,0.5,4.0,8.0]
spl_linear= sci.InterpolatedUnivariateSpline(x,y,k=1)
spl_quadratic= sci.InterpolatedUnivariateSpline(x,y,k=2)    
lag=sci.lagrange(x,y)
xnew=np.arange(0,5,.001)
plt.scatter(x,y)
plt.plot(xnew,spl_linear(xnew),xnew,spl_quadratic(xnew),xnew,spl_cubic(xnew),xnew,lag(xnew),'--')
plt.legend(['linear_spline','quadratic_spline','cubic_spline','lagrange'],loc='best')
plt.title('Spline and Lagrange Interpolated Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
