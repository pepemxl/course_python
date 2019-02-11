# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 00:26:49 2019

@author: José Luis Alonzo Velázquez
@email: pepemxl@gmail.com
"""
# Universal Functions
import numpy as np


a = np.arange(1,11)
print(a)
#[ 1  2  3  4  5  6  7  8  9 10]
print(np.log(a))
#[0.         0.69314718 1.09861229 1.38629436 1.60943791 1.79175947
# 1.94591015 2.07944154 2.19722458 2.30258509]
print(np.sin(a))
#[ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427 -0.2794155
#  0.6569866   0.98935825  0.41211849 -0.54402111]
print(np.sqrt(a))
#[1.         1.41421356 1.73205081 2.         2.23606798 2.44948974
# 2.64575131 2.82842712 3.         3.16227766]
print(a.sum())
#55
print(a.min())
#1
print(a.max())
#10
print(a.mean())
#5.5
print(a.std())
#2.8722813232690143
