# Write a program to check the leap year or not

year = int(input("Enter year: "))

# for century
if ( year % 100 == 0 and year % 400 == 0 ):
    print(f"{year} a is century leap year")
elif ( year % 100 != 0 and year % 4 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year") 

# complete