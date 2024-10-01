# Write a program to check a prime number or not

num = int(input("Enter num value: "))
status = ""

if num >= 0:
    if num == 0 or num == 1:
        status = "n2"
    else:
        for x in range(2, num): # error 2 not store in x (check and study range)
            if num % x == 0:
                status = "n3"
                break
            else: 
                status = "n4"
else:
    print("Error: Enter Whole Number")  

if status == "n2":
    print(f"{num} is not a prime or composite number")
elif status == "n3":
    print(f"{num} is not a prime number")   
elif status == "n4" :
    print(f"{num} is a prime number") 
