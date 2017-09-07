word = "sditmsgjdsffghd"
dict = {}
for c in word:
    if c in dict:
        dict[c] +=1
    else:
        dict[c] = 1
print(dict)
