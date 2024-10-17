#Task 7
from operator import contains

vowels = ["a", "e", "i", "o", "u"]
vowelnum = 0

inputstr = input("Please input something: ").lower()

for i in range(len(inputstr)):
    if contains(vowels,inputstr[i]):
        vowelnum = vowelnum+1

print(vowelnum)

#Task 8
import re
pracstring = input("Hello World")

print(pracstring.replace('l','w'))

#Task 9
sentence1 = input("Write a sentence: ")

wordlist = sentence1.split(' ')

print(max(wordlist, key = len))