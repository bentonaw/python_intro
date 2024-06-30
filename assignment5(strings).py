continue_program = "y"

while continue_program == "y":
    table_number = int(input("Enter a multiplication table: "))
    start_interval = int(input("Enter the start interval: "))
    stop_interval = int(input("Enter the stop interval: "))
    print("----------------------")
    print(f'Table of {table_number}')
    print("----------------------")

    stop_interval_length = len(str(stop_interval))
    sum_length = len(str(stop_interval * table_number)) + 1

    for i in range(start_interval, stop_interval + 1):
        print(f'{i:{stop_interval_length}} * {table_number} = {i * table_number:{sum_length}}')

    end_program = "x"
    
    while end_program != "y" and end_program != "n":
        end_program = input("\nDo you want to end program (y/n)? ").lower()
        if end_program == "y":
            continue_program = "n"
            print("Program terminated!")
        elif end_program == "n":
            print()
        else:
            print("Invalid response")
