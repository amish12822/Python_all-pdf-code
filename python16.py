# Write a program to print the factorial of take a number from the user

num = int(input("Enter number: "))
sum = 1

for x in range(1, num+1):
    sum = sum * x

print(f"Factorial of {num} is: {sum}")

#   Complete