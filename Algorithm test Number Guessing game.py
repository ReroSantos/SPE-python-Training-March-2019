# Paste your code into this box
print("Please think of a number between 0 and 100!")
guess = 50
low = 0
high = 100
while True:
    print ("Is your secret number", guess, end = "")
    print ("?")
    verify = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if verify == "h":
        high = guess
        guess = (high+low)//2
        
    elif verify == "l":
        low = guess
        guess = (high + low)//2
    
    elif verify == "c":
        print("Game over. Your secret number was:",guess)
        break
        
    else:
        print("Sorry, I did not understand your input.")