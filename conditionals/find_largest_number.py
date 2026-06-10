num_1 = float(input("enter the first number : "))
num_2 = float(input("enter the second number : "))
num_3 = float(input("enter the third number : "))

if num_1>num_2 and num_1>num_3:
    print(f"{num_1} is the largest number")
elif num_2>num_1 and num_2>num_3:
    print(f"{num_2} is the largest number")
else:
    print(f"{num_3} is the largest number")