# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import Counter
def repeatedword(sentence):
    words = list(sentence.split(" "))
    s = Counter(words)
    for i in words:
        if(s[i] > 1):
            return 'No'
    return 'yes'
sentence = input("")
print(repeatedword(sentence))
