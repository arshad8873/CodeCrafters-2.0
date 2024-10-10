#print("Hello World")
#print(2+43)
"""
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


print("\n\t\t\t CALCULATOR SIMULATOR")
print("\t\t\t ********************\n")
print("\t\t\t  1: Addition")
print("\t\t\t  2: Substraction")
print("\t\t\t  3: Division")
print("\t\t\t  4: Multipication")
print("\t\t\t  5: Modulas")
print("\t\t\t  6: Floor Division")
print("\t\t\t  7: Exponential\n")


while True: 
        ch=int(input("Enter your choice(1-7): "))
        num_1: float=float(input("Enter the number: "))
        num_2: float=float(input("Enter another number: "))  


        if ch==1:
           Sum=num_1 + num_2
           print(f"\n{num_1} + {num_2} = {Sum}\n")


        elif ch==2:
            Sub=num_1 - num_2
            print(f"\n{num_1} - {num_2} = {Sub}\n") 


        elif ch==3:
                Div=num_1/num_2
                print(f"\n{num_1} / {num_2} = {Div}\n")


        elif ch==4:
                Mul=num_1 * num_2
                print   (f"\n{num_1} * {num_2} = {Mul}\n") 

        elif ch==5:
                 Mod=num_1 % num_2
                 print(f"\n{num_1} % {num_2} = {Mod}\n")  


        elif ch==6:
                 Flo=num_1 // num_2
                 print(f"\n{num_1} // {num_2} = {Flo}\n")


        elif ch==7:
                 Expo=num_1 ** num_2
                 print(f"\n{num_1} ** {num_2} = {Expo}\n")

        else:
                print("wrong value")
                break 
      _______________________________________          
                        
i=1
while i <10:
        print(i, "hooo")
        i = i + 2

print(i, "hooo") 

for i in range(0,10,2):
        print(i,"colour")               
     _______________________________________

ab = 10
bc = 20

def number_add(a,b):
        sum = a + b
        return sum

new_sum = number_add(ab, bc)

print(new_sum)
______________________________________
import random

x = random.random()
print(x)
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug = True)        