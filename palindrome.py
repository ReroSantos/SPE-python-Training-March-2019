import string

def is_palindrome(sentence):
    c = -1
    
    alpha = string.ascii_lowercase
    holder = sentence.lower()
    sentence = ""
    for i in holder:
        if i in alpha:
            sentence += i

    for i in sentence:
        if sentence[c] != i:
            return False
        else:
            c -= 1
    return True
        