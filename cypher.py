import string

def cypher(word, shift):
    """
    word : The word you want to perform the encryption upon
    shift : a positive integer that denotes the factor of shift
    """

    def cypherDict(shift):
        holder = {}
        trip = 0
        trip2 = 0
        
        lowerKeys = string.ascii_lowercase
        upperKeys = string.ascii_uppercase
        
        for i in lowerKeys:
            holder[i] = lowerKeys[trip - 26 + shift]
            trip += 1
        
        for i in upperKeys:
            holder[i] = upperKeys[trip2 - 26 + shift]
            trip2 += 1
        
        holder[" "] = " "
        return holder

    def cypherGen(word):
        holder = cypherDict(shift)
        container = ''
        for i in word:
            container += holder[i]

        return container

    return cypherGen(word)