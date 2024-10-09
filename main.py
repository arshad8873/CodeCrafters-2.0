#print("Hello World")
#print(2+43)

name: str = input("enter your name: ") 
print(f"The Name is {name}")
num_1: int = int(input("enter a number 1: "))
num_2: int = int(input("enter a number 2: "))

if num_1==num_2:
    print("the number is same")
elif num_1>num_2:
    print(f"{num_1} is greater") 
else:
    print(f"{num_2} is greater")
