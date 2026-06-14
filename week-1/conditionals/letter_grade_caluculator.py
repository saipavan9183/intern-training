# letter grade caluculator
score = int(input("enter the score : "))

if score>90:
    print("your grade is A")
elif score>75 and score<=90:
    print("your grade is B")
elif score>65 and score<=75:
    print("your grade is C")
elif score>50 and score<=65:
    print("your grade is D")
elif score<35 and score>=0:
    print("your grade is F")
else:
    print("enter correct score")
