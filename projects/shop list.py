shop_list = {}


def show_list (sample_list):
    item_count = 0
    price_count = 0
    for item , price in sample_list.items():
        item_count += 1 
        price_count += price
        print(f'{item} : {price}')
        
    print(f'count of your items : {item_count}')
    print(f"total price {price_count}")

def add_list (item , price , sample_list):
    sample_list[item] = price


def search (item , sample_list):
    if item in sample_list:
        print(f'{item} in your list is : {sample_list[item]}')
    else :
        print("you dont have this item")



shop = True

while shop :
    item= input("what do you buy : ")
    
    if item == "end" :
        show_list(shop_list)
        break
    
    elif item == "search" :
        user_input = input("enter the item to search : ")
        search(user_input , shop_list)
    
    else :
        price = int(input("enter the price : "))
        add_list(item , price , shop_list)
        print("item added")
