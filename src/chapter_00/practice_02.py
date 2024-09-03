# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 00:07:49 2019

@author: José Luis Alonzo Velázquez
@email: pepemxl@gmail.com
"""
# Aritmetic Operators
a = np.arange(5)
print(a)
#[0 1 2 3 4]
print(a+4)
#[4 5 6 7 8]
print(a*4)
#[ 0  4  8 12 16]
b = np.arange(5, 10)
print(b)
#[5 6 7 8 9]
print(a+b)
#[ 5  7  9 11 13]
print(a-b)
#[-5 -5 -5 -5 -5]
print(a*b)
#[ 0  6 14 24 36]
print(a*np.sin(b))
#[-0.         -0.2794155   1.3139732   2.96807474  1.64847394]
print(a*np.sqrt(b))
#[ 0.          2.44948974  5.29150262  8.48528137 12.        ]
A = np.arange(1, 10).reshape(3, 3)
print(A)
#[[1 2 3]
# [4 5 6]
# [7 8 9]]
B = np.ones((3, 3))
print(B)
#[[1. 1. 1.]
# [1. 1. 1.]
# [1. 1. 1.]]
print(A*B)
#[[1. 2. 3.]
# [4. 5. 6.]
# [7. 8. 9.]]
print(np.dot(A, B))
#[[ 6.  6.  6.]
# [15. 15. 15.]
# [24. 24. 24.]]
print(A.dot(B))
#[[ 6.  6.  6.]
# [15. 15. 15.]
# [24. 24. 24.]]
A += 1
print(A)
#[[ 2  3  4]
# [ 5  6  7]
# [ 8  9 10]]
A -= 1
print(A)
#[[1 2 3]
# [4 5 6]
# [7 8 9]]
A *= 2
print(A)
#[[ 2  4  6]
# [ 8 10 12]
# [14 16 18]]
