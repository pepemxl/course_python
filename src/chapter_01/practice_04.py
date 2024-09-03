#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:01:37 2019


@author: José Luis Alonzo Velázquez
@email: pepemxl@gmail.com
@title: Practice 04: Indexing, Slicing, and Iterating from book Python Data Analytics
"""
import numpy as np


if __name__ == '__main__':
  a = np.arange(10, 16)
  print(a)
#  [10 11 12 13 14 15]
  print(a[4])
#  14
  print(a[-1])
#  15
  print(a[-2])
#  14
  print(a[[4, -2, -1]])# accesing multiple values
#  [14 14 15]
  print(a[1:5:2])
#  [11 13]
  print(a[::2])
#  [10 12 14]
  print(a[:5:2])
#  [10 12 14]
  print(a[:5:])
#  [10 11 12 13 14]
  A = np.arange(10, 19).reshape((3, 3))
  print(A)
#[[10 11 12]
# [13 14 15]
# [16 17 18]]
  print(A[0, :])
#  [10 11 12]
  print(A[:, 0])
#  [10 13 16]
  print(A[0:2, 0:2])
#[[10 11]
# [13 14]]
  print(A[[0,2], 0:2])
#[[10 11]
# [16 17]]
  