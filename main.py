import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
num_letters = int(input("How many numbers would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))

password = []

for i in range(0,num_letters):
    password.append(letters[random.randint(0,51)])

for i in range(0,num_numbers):
    password.append(numbers[random.randint(0,9)])

for i in range(0,num_symbols):
    password.append(symbols[random.randint(0,8)])

random.shuffle(password)
final_password=""

for i in range(0,len(password)):
    final_password += password[i];

print(final_password)
