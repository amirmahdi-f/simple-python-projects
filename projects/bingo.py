from random import randint


real_num = randint(1 , 100)


play = True
while play :
    user_guess = int(input("enter your guess : "))
    
    if user_guess == real_num :
        print("you won !!?")
        paly = False
        
    if user_guess > real_num :
        print("go Down")
        
    if user_guess < real_num :
        print("go Up")
        
