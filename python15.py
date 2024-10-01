# Write a program to print all prime number in an interval of 1-10
a = int(input("Enter initial number: "))
b = int(input("Enter end number: "))

for x in range(a, b+1):

    if x>1:

        for y in range(2, x):
            if x % y == 0:
                break
        else:
            print(x)

#   complete