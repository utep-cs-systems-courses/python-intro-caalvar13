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
    
    
    
    