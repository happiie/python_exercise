# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:47:15 2018

@author: AKMAL FARHAN
"""

import math
import numpy

print("***Complex Number in Polar Form ***")

cmplx = complex(input("Please enter a complex number: "))

m = math.sqrt(cmplx.real*cmplx.real + cmplx.imag*cmplx.imag)


print("\n***Complex Number in Polar Form ***")
print('Please enter a complex number: ', cmplx)
print('The complex number in polar form')

print('m = ', m)

if cmplx.real > 0:
    p = numpy.arctan(cmplx.imag/cmplx.real)
    print('p = ',p)
    
else:
    p = numpy.arctan(cmplx.imag/cmplx.real) + math.pi
    print('p = ',p)
    
print('*** End ***')