__author__ = 'mohamed'

def anti_vowel(text):

    for i in text:
        l = i.lower()
        if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
           text = text.replace(i, '')
    return text

print anti_vowel('hello')
