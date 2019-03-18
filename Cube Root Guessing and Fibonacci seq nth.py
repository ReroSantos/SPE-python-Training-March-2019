#root guess
'''
x = int(input('Enter an integer: '))
ans = 0

while ans**3 < x:
    ans += 1
    
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
    
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))

'''









#fib

x = int(input('Enter an integer: '))

a = 0
b = 1

for i in range(x):
    ans = a
    c = b + a
    a,b = b,c
    
print(ans)
