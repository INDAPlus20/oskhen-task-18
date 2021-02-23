#!/usr/bin/env python3

token = open("token", "r", encoding="ISO-8859-1").readlines()
index = open("index", "w", encoding="ISO-8859-1")

word = ""
numbers = list()

for line in token:
    x = line.strip("\n").split(" ")
    if x[0] == word:
        numbers.append(x[1])
    else:
        index.write(f"{word} {' '.join(numbers)}\n")
        numbers = list()
        word = x[0]
        numbers.append(x[1])