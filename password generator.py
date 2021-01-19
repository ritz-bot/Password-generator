
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nl= int(input("How many letters would you like in your password?\n")) 
ns = int(input(f"How many symbols would you like?\n"))
nn = int(input(f"How many numbers would you like?\n"))


password_list=[]

for char in range(1,nl+1):
    password_list.append(random.choice(letters))
    
for char in range(1,nn+1):
    password_list.append(random.choice(numbers))

for char in range(1,ns+1):
    password_list.append(random.choice(symbols))
    
    
print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
    password+=char
    
print(password)
    