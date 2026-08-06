from tkinter import * 
from test import *

xo_table = [['1' , '2' , '3'],
            ['4' , '5' , '6'],
            ['7' , '8' , '9']]


def show_tutorial ():
    show("player_1 : X  |  player_2 : O")
    
def print_XO():
    print('        |       |       ')
    print(f'   {xo_table[0][0]}    |   {xo_table[0][1]}   |    {xo_table[0][2]}  ')
    print('        |       |       ')
    print('--------+-------+--------')
    print('        |       |       ')
    print(f'   {xo_table[1][0]}    |   {xo_table[1][1]}   |    {xo_table[1][2]}  ')
    print('        |       |       ')
    print('--------+-------+--------')
    print('        |       |       ')
    print(f'   {xo_table[2][0]}    |   {xo_table[2][1]}   |    {xo_table[2][2]}  ')
    print('        |       |       ')

def win (player):
    print(f'{player} win !!!')
    
def check_full (table):
    full_list = []
    count = 0 
    for x in range (0 , 3):
        for y in range (0 , 3):
            if table[x][y] == 'X' or table[x][y] == "O":
                count += 1
                full_list.append(count)
                
    if full_list == [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8  , 9]:
        return True
def check (table):
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2]:
            print("raw completed")
            exit(0)
        if table[0][i] == table[1][i] == table[2][i]:
            print("column completed")
            exit(0)
        if table[0][0] == table[1][1] == table[2][2]:
            print("diameter completed")
            exit(0)
        if table[0][2] == table[1][1] == table[2][0]:
            print("diameter completed")
            exit(0)
    else : 
        if check_full(table) :
            print("draw")
            exit(0)
def choice (table , user_choice , player_icon):
    if (user_choice-1) // 3 == 0 :
        if (table[(user_choice-1) // 3][user_choice-1] != 'X' and  table[(user_choice-1) // 3][user_choice-1] != 'O'):
            table[(user_choice-1) // 3][user_choice-1] = player_icon
    elif (user_choice-1) // 3 == 1 :
        if (table[(user_choice-1) // 3][user_choice-4] != 'X' and table[(user_choice-1) // 3][user_choice-4] != 'O'):
            table[(user_choice-1) // 3][user_choice-4] = player_icon
    elif (user_choice-1) // 3 == 2 :
        if (table[(user_choice-1) // 3][user_choice-7] != 'X' and table[(user_choice-1) // 3][user_choice-7] != 'O'):
            table[(user_choice-1) // 3][user_choice-7] = player_icon
    else : 
        print(f'{user_choice} is for another player and you lost your chance')
show_tutorial()

def choice_button(button_num, xo_table):
    choice(xo_table, button_num, 'X')

play = True
# while play :
#     print_XO()
#     player_1_choice = int(input('player_1 choice : '))
#     choice(xo_table , player_1_choice , 'X')
#     print_XO()
#     check(xo_table)
#     player_2_choice = int(input('player_2 choice : '))
#     choice(xo_table , player_2_choice , 'O')
#     check(xo_table)
    
    
    
window = Tk()


button_1 = Button(text=xo_table[0][0], command= choice_button(1, xo_table))
button_2 = Button(text=xo_table[0][1], command= choice_button(2, xo_table))
button_3 = Button(text=xo_table[0][2], command= choice_button(3, xo_table))
button_4 = Button(text=xo_table[1][0], command= choice_button(4, xo_table))
button_5 = Button(text=xo_table[1][1], command= choice_button(5, xo_table))
button_6 = Button(text=xo_table[1][2], command= choice_button(6, xo_table))
button_7 = Button(text=xo_table[2][0], command= choice_button(7, xo_table))
button_8 = Button(text=xo_table[2][1], command= choice_button(8, xo_table))
button_9 = Button(text=xo_table[2][2], command= choice_button(9, xo_table))


button_1.place(x=10 , y=10)
button_2.place(x=30 , y=10)
button_3.place(x=50 , y=10)
button_4.place(x=10 , y=40)
button_5.place(x=30 , y=40)
button_6.place(x=50 , y=40)
button_7.place(x=10 , y=70)
button_8.place(x=30 , y=70)
button_9.place(x=50 , y=70)

mainloop()