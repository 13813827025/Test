# yangli
import getpass

myage = 19

guess = int(input("age:"))

if guess == myage :
    print("you get it")
elif guess>myage :
    print("think smaller")
else:
    print("think biger")

while True:
    guess = int(input("age:"))
    if guess == myage :
        print("you get it")

