# Write a program to swap variable with used third variabl

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

print(f"Original value: a = {a}, b = {b}")

a , b = b , a

print(f"Swap value: a = {a}, b = {b}") 