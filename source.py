import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level generator
password = "" # To store password

# Picking random letters using for loop
for var in range(0, nr_letters):
    password += random.choice(letters)
    # print(password)
    
# Picking up random symbols using for loop
for var in range(0, nr_symbols):
    password += random.choice(symbols)
    # print(password)
    
# Picking up random numbers using for loop
for var in range(0, nr_numbers):
    password += random.choice(numbers)
    # print(password)
    
# Print out the password
print(f"Easy password : {password}")



# Hard Level generator
password_list = [] # This will use the list to shuffle and create harder passwords

# Picking random letters using for loop
for var in range(0, nr_letters):
    password_list.append(random.choice(letters)) # Appending the coming random items into the list
    # print(password)
    
# Picking up random symbols using for loop
for var in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
    # print(password)
    
# Picking up random numbers using for loop
for var in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
    # print(password)
    
# Shuffling the password
random.shuffle(password_list)

    
Final_Password = "" # Variable to store final password

# Using for loop to assign all the elements of list to variable
for item in password_list:
    Final_Password += item # Assignment
    
# Print out the final password
print(f"Hard password : {Final_Password}")
 
