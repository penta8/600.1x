#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 21:55:00 2017

@author: yango
"""

s = 'azcbobobegghakl'
vowels = 0

for letter in s:
    if letter in 'aeiou':
        vowels += 1

print('Number of vowels: ' + str(vowels))