#!/usr/bin/env python3

margin = 20

def search(word):

    magicFILE = open("magic", "r", encoding="ISO-8859-1").readlines()

    index = None
    prefix = word[0:3]

    for line in magicFILE:
        x = line.split(" ")
        if x[0] == prefix:
            index = int(x[1])
            break

    if not index:
        print(f"Word '{word}' not found!")
        exit()

    indexFILE = open("index", "r", encoding="ISO-8859-1")
    korpus = open("korpus", "r", encoding="ISO-8859-1")
    indexFILE.seek(index)

    while True:
        line = indexFILE.readline().split(" ")
        currentWord = line[0]
        occurances = line[1:]

        if currentWord == word:
            print(f"Word {word} occurs {len(occurances)} times:")
            for occurance in occurances:
                korpus.seek(int(occurance.strip("\n")) - margin)
                segment = korpus.read(margin*2).replace("\n","|")
                print(segment)
            break
        elif line[0][0:3] != prefix:
            print("word not found!")
            break

if __name__ == "__main__":
    x = input("Search for what word?\n")
    search(x)


    

