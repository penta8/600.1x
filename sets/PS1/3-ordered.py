#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:26:05 2017

@author: yango
"""
s = 'azcbobobegghakl'

ordered = ''
index = 0

for letter in s:
    lastLetter = ''
    tempOrdered = ''
    
    for subLetter in s[index:]:
        if subLetter >= lastLetter:
            tempOrdered += subLetter
            lastLetter = subLetter
        else:
            break
    
    if len(tempOrdered) > len(ordered):
        ordered = tempOrdered
    
    index += 1

print('Longest substring in alphabetical order is: ' + ordered)