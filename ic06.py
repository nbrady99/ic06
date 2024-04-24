#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:54:34 2024

@author: nbrady

ic06 Assignment
"""

def countWords(file):
    lyrics = file.split()
    count = { }
    
    for word in lyrics:
        if (word in count):
            count[word] += + 1
        else:
            count[word] = 1

    return count

def wordCompare(userLyrics, artistLyrics):
    lyrics = userLyrics.split()
    compare = 0
    
    for word in lyrics:
        compare += artistLyrics.get(word, 0)    
    return compare
    

def main():
    
    # Input from user
    artist1 = input("Artist 1: ")
    artistFile1 = input("Artist 1 lyric file: ")
    artist2 = input("Artist 2: ")
    artistFile2 = input("Artist 2 lyric file: ")
    userLyric = input("Input lyric (NO punctuation) to predict: ")
    
    # Open files
    fileHandle1 = open(artistFile1, encoding="utf8")
    fileHandle2 = open(artistFile2, encoding="utf8")

    # Read files
    readFile1 = fileHandle1.read()
    readFile2 = fileHandle2.read()
    
    # Count the word occurence
    words1 = countWords(readFile1)
    words2 = countWords(readFile2)

    # Close files
    fileHandle1.close()
    fileHandle2.close()

    # Compare words
    wordCompare1 = wordCompare(userLyric, words1)
    wordCompare2 = wordCompare(userLyric, words2)
    
    if (wordCompare1 > wordCompare2):
        print(artist1, "probably wrote that song!")
    else: print(artist2, "probably wrote that song!")


if __name__ == "__main__":
    main()

