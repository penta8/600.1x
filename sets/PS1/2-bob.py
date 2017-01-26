#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:03:45 2017

@author: yango
"""

s = 'azcbobobegghaklbobob'
word = 'bob'
counter = 0
total_word = 0

while counter < len(s):
    if s[counter:counter+3] == word:
        total_word += 1
    counter += 1

print('Number of times bob occurs is: ' + str(total_word))