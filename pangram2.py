import string

def is_pangram(sentence):
    alphabet = string.ascii_lowercase
    pangram = sentence.lower()
    
    for i in alphabet:
        if i not in pangram:
            return False
    
    return True