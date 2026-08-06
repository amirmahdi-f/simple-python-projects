import json

phone_list = {"amirmahdi" : 123, "amirali" : 1234}

def menu ():
    print("--------------------------------------------------")
    print("|  add  |  remove  |  search  | show-all |  end  |")
    print("--------------------------------------------------")
    
def add (phone_list , name , number) :
    phone_list[name] = number
    
def remove (phone_list , name) :
    phone_list.pop(name)

def show_all (phone_list) :
    for name , number in phone_list.items():
        print(f'{name} : {number}')
        

def search (phone_list , name) :
    if name in phone_list :
        print(f"{name} is in your list")
    else :
        print(f"{name} isn't in your list")
        
def write_json (phone_list):
    print("phone list added to phone_book.txt")
    with open ("phone_book.txt", "w") as file:
        file.write(json.dumps(phone_list))

want_to_use = True

while want_to_use:
    menu()
    process = input("what do you want to do ? ")
    
    if process == "add":
        name = input("enter the name : ")
        number = int(input(f"enter the {name}'s number : "))
        add(phone_list , name , number)
    
    elif process == "remove" : 
        name = input("enter the name : ")
        remove(phone_list , name)
        
    elif process == "search":
        name = input("enter the name : ")
        search(phone_list , name)
        
    elif process == "show-all":
        show_all(phone_list)
    
    elif process == "end":
        break
        write_json(phone_list)
    
    else : 
        print("this command did not defined !!?")
        
    write_json(phone_list)
    print("process finished.")