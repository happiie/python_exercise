# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 12:25:45 2018

@author: AKMAL FARHAN
"""
student={}

student['sid'] = input("Student ID: ")
student['n'] = input("Name: ")
student['d'] = input("Date of Birth: ")
student['h'] = int(input("Height: "))
student['w'] = int(input("Weight: "))

print('***Welcome to Deparment of Electrical Engineering***')
print("Student ID: ",student['sid'])
print("Name: ",student['n'])
print("Date of Birth: ",student['d'])
print("Height: ",student['h'])
print("Weight: ",student['w'])
print("*** End ***")