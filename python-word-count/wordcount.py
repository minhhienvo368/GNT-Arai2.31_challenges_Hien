# Write a program that given a phrase can count the occurrences
# of each word in that phrase
import numpy

def word_count(text: str) -> dict:
    counts = dict()
    phrase = text.split()
    for word in phrase:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
#word_count('one fish two fish red fish blue fish')

your_phrase = 'rah rah ah ah ah\troma roma ma\tga ga oh la la\t'
your_phrase = 'testing 1 2 testing'
word_count(your_phrase)