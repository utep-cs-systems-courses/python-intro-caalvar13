#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:00:09 2020

@author: calvar13
"""
import sys        # command line arguments
import re         # regular expression tools

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Correct usage: wordCountTest.py <input text file> <output file>")
        sys.exit()
    
    inputFile = open(sys.argv[1], 'r')
    
    words = inputFile.read()
    inputFile.close()
    
    words = re.sub(r'[^\w\s]', '', words)
    words = words.strip()
    words = re.split('[ \n]', words)
    
    dict = {}
    
    for word in words:
        if word == '':
            continue
        if word.lower() in dict.keys():
            dict[word.lower()] += 1
        else:
            dict[word.lower()] = 1
                
    dict = sorted(dict.items()) 
    
    
    