def gcd(x,y):
    if x > y:
        a, b = x, y
    else:
        b, a = x, y

    r = a % b
    if r == 0:
        return b

    else:
        while r  != 0:
            r= a % b
            a, b = b, r

        return a

gcd(100, 450)

gcd(100,50)