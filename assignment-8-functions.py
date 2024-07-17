def print_max(a,b,c):
    if a >= b and a >= c:
        largest_num = a
    elif b >= a and b >= c:
        largest_num = b
    else:
        largest_num = c
    print(f"The largest number is: {largest_num}")

value_1 = int(input("Enter first number: "))
value_2 = int(input("Enter second number: "))
value_3 = int(input("Enter third number: "))
print_max(value_1,value_2,value_3)