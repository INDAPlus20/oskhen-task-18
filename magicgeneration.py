#!/usr/bin/env python3

indexFILE = open("index", "rb").read().split(b'\n')
magic = open("magic", "w", encoding="ISO-8859-1")

prefix = ""
counter = 0
for line in indexFILE:
    word = ""
    index = counter
    flag = False
    for b in line:
        if flag:
            counter += 1
            continue

        if b != ord(" "):
            word += chr(b)
        else:
            if word[0:3] != prefix:
                magic.write(f"{word[0:3]} {str(index)}\n")
            flag = True

        counter+=1
    prefix = word[0:3]
    counter += 1

def value(c):
    if c not in "åäö":
        return ord(c) - ord('a')
    elif c == 'å':
        return 26
    elif c == 'ä':
        return 27
    elif c == 'ö':
        return 28

def hash(wordslice):
    return sum([value(c) for c in wordslice])
