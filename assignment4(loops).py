count = 0
total = 0

continue_calculation = "y"
while continue_calculation == "y":
    integer_value = int(input("Enter a positive integer to calculate sum and average: "))

    if integer_value > 0:
        count += 1
        total += integer_value
    elif integer_value < 0:
        print("Negative numbers are not included in the sum!")
    elif integer_value == 0 and count == 0:
        continue_calculation = input("Do you want to calculate another sum and average (y/n)? ")
    elif integer_value == 0 and count != 0:
        print("The sum of the entered integers is:", total)
        average = total / count
        print("The average of the entered integers is:", average)

        total = 0
        count = 0

        continue_calculation = input("Do you want to calculate another sum and average (y/n)? ")

print("Ending program!")
