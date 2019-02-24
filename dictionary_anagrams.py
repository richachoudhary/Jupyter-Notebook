# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 14:05:25 2019

@author: RICHA
"""

import urllib.request
import collections

wordclean = sorted(list(set([word.strip().lower().decode("utf-8") for word in urllib.request.urlopen('https://engmrk.com/wp-content/uploads/2018/06/anagrams.csv')])))
print(type(wordclean))
#Define function that returns the word whose words are sorted alphabetically.
#def signature(word): return ''.join(sorted(word))

#Define a dict variable
#words_bysig = collections.defaultdict(list)

#Use for loop to create your dictionary
#for word in wordclean: words_bysig[signature(word)].append(word)

#Now define an anagram function.
#def anagram(word): return words_bysig[signature(word)]

#anagram('eagle')