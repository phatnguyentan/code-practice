#!/bin/python3

import sys

# print("pangram") if len(set([i.lower() for i in input().strip()]) & set("abcdefghijklmnopqrstuvwxyz")) == 26  else print("not pangram")
 #
 # if (len(set([i.lower() for i in "We promptly judged antique ivory buckles for the next prize"]) & set("abcdefghijklmnopqrstuvwxyz")) == 26):
 #     return true
 # else:
 #     return false


s = input()
exists = set()

for char in s:
    exists.add(char.lower())

for i in range(ord('a'), ord('z') + 1):
    if not chr(i) in exists:
        print("not pangram")
        break
else:
    print("pangram")
