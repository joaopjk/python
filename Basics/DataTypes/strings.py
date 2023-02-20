my_strings = "Hello World"
print(my_strings[0])
print(my_strings[-1])
print(my_strings[:3])
print(my_strings[::-1])  # reverse string

for char in my_strings:
    print(char)

# Immutability
name = "Joao"
# name[0] = "T" Error, because strings are immutable
last_letters = name[1:]
print("P"+last_letters)
last_letters = "P" + last_letters
print(last_letters)