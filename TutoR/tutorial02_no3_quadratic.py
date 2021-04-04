# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 16:00:29 2018

@author: AKMAL FARHAN
"""
import math

print('***Quadratic Equation Solver***')
print('Please key in the following quadratic equation coefficients')
a = float(input('a : '))
b = float(input('b : '))
c = float(input('c : '))

delta = b*b-4*a*c

print('\n***Quadratic Equation Solver***')
print('Please key in the following quadratic equation coefficients')
print('a : ',a)
print('b : ',b)
print('c : ',c)
print('The solutions for the quadratic equations are')

if delta < 0:
    print('No solutions for real number.')
    x1 = -b/2*a
    x2 = pow(delta,0.5)/(2*a)
    print('But, there are distinct complex number:')
    print('1st complex number = ',x1,'+',x2.imag)
    print('2nd complex number = ',x1,'-',x2.imag)

elif delta > 0:
    print('Two distinct real number.')
    x2 = (-b + math.sqrt(delta)) / 2*a
    x1 = (-b - math.sqrt(delta)) / 2*a
    print('x1 = ', x1)
    print('x2 = ', x2)
    
elif delta == 0:
    print('One real number only.')
    x1 = (-b - math.sqrt(delta)) / 2*a
    print('x1 = ', x1)
    

    
    
