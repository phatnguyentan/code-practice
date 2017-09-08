#!/bin/python3

import sys

def super_reduced_string(s):
    # Complete this function
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s = s[:i] + s[i+2:]
            i = 0
        else:
            i += 1
    if len(s) == 0:
        s = "Empty String"
    return s

# s = "aaabccddd"
# s = "bb"
# s = "baab"
s = "acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj"
# acdqgacdqj
result = super_reduced_string(s)
print(result)
