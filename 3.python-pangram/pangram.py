# Write a program check if a string is a pangram
import string
import re

def strip_punctuation(word: str) -> str:  #eleminate puntuation function
    exclude = set(string.punctuation)
    word = ''.join(char for char in word if char not in exclude)
    return word

def is_pangram(text: str) -> bool:
    text = re.sub('"', '', text)
    text = text.rstrip()
    text = strip_punctuation(text.lower())
    for char in string.ascii_lowercase:
        if char not in text:
            return False
    return True

is_pangram("'Victor jagt zwölf Boxkämpfer quer über den' ' großen Sylter Deich.'")

# COACHES' NOTE: Very clean and nice code. No remarks.
