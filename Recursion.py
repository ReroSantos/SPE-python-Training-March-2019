'''def iteradd(digit, difference):
    holder = (digit while digit > 0 if digit -= difference)

    return sum(list(holder))
'''


def iteradd(digit, difference):
    holder = []
    #container = 0

    while digit > 0:
        holder.append(digit)
        digit = digit - difference

    '''for numbers in holder:
        container = container + numbers
    
    return container'''
    return sum(holder)

def iteradd2(digit, difference):
    container = digit

    if (digit - difference) <= 0:
        return container
    else:
        digit = digit - difference
        return container + iteradd2(digit, difference)


def factorial(number):
    container = number
    if (number - 1) <= 0:
        return 1
    else:
        bubble = number - 1
        return container * factorial(bubble)
