# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 23:32:18 2019

@author: José Luis Alonzo Velázquez
@email: pepemxl@gmail.com
"""
import numpy as np

# Create an array
a = np.array([1, 2, 3])
print(a)
# [1 2 3]
print(type(a))
# <class 'numpy.ndarray'>
print(a.dtype)
# int32
print(a.ndim)
# 1
print(a.size)
# 3
print(a.shape)
#(3,)
b = np.array([[1., 2, 3], [5, 6, 7]])
print(b)
# [[1. 2. 3.] 
#  [5. 6. 7.]]
print(type(b))
# <class 'numpy.ndarray'>
print(b.dtype)
# float64
print(b.ndim)
# 2
print(b.size)
# 6
print(b.shape)
#(2, 3)
print(b.itemsize)
# 8
print(b.data)
# <memory at 0x000001DDD3115CF0>
c = np.array(['a', 'b', 'c'])
print(c)
# ['a', 'b', 'c']
print(c.dtype)
# <U1
print(c.dtype.name)
# str32
d = np.array([[1, 2, 3],[4, 5, 6]], dtype=complex)
print(d)
#[[1.+0.j 2.+0.j 3.+0.j]
# [4.+0.j 5.+0.j 6.+0.j]]
e = np.zeros((3, 3))
print(e)
#[[0. 0. 0.]
# [0. 0. 0.]
# [0. 0. 0.]]
f = np.ones((3, 3))
print(f)
#[[1. 1. 1.]
# [1. 1. 1.]
# [1. 1. 1.]]
g = np.arange(0, 10)
print(g)
#[0 1 2 3 4 5 6 7 8 9]
h = np.arange(0, 10, 3)
print(h)
#[0 3 6 9]
i = np.arange(0, 10, 0.5)
print(i)
#[0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5 5.  5.5 6.  6.5 7.  7.5 8.  8.5
# 9.  9.5]
j = np.arange(0, 20).reshape(5, 4)
print(j)
#[[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]
# [12 13 14 15]
# [16 17 18 19]]
k = np.linspace(0, 10, 5)
print(k)
# [ 0.   2.5  5.   7.5 10. ]
l = np.random.random(3)
print(l)
#[0.39560131 0.48102535 0.54183932]
m = np.random.random((3,3))
print(m)
#[[0.29116808 0.44571308 0.18904856]
# [0.58562459 0.73452366 0.66553058]
# [0.85903456 0.60606405 0.88251218]]
