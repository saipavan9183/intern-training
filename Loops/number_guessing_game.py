num = 0
i=79
while True:
    num = int(input("Guess the number : "))
    if i==num:
        print("correct")
        break
    elif num>i:
        print("wrong number try lower")
    elif num<i:
        print("wrong number try higher")
    
