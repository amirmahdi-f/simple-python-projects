def calculate (num_1 , num_2 , process):
    if process == "*":
        return (num_1 * num_2)
    if process == "/":
        return (num_1 / num_2)
    if process == "+":
        return (num_1 + num_2)
    if process == "-":
        return (num_1 - num_2)    
    
    
num_1 , process , num_2 = input().split(sep=" ")

num_1 = int(num_1)
num_2 = int(num_2)

print(calculate(num_1 , num_2 , process))