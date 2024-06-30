result = int(input("Enter your score: "))

if 48 <= result <= 50:
    print("Your grade is: A")
elif 40 <= result <= 47:
    print("Your grade is: B")
elif 32 <= result <= 39:
    print("Your grade is: C")
elif 24 <= result <= 31:
    print("Your grade is: D")
elif 16 <= result <= 23:
    print("Your grade is: E")
elif 0 <= result <= 15:
    print("Your grade is: F")
else:
    print("Invalid score for a grade result")
