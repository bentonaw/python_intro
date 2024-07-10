running = True
method_allowed = ("+", "-", "*", "/", "%", "//")

while running:
    answer = None

    repeat_first_prompt = True
    while repeat_first_prompt:
        first_operand = input("Enter operand: ")
        try:
            first_operand = int(first_operand)
            repeat_first_prompt = False
        except ValueError:
            print(f"{first_operand} is not a valid input. Please enter a number.")

    method = input(" | ".join(method_allowed) + ", Choose calculation method: ")
    while method not in method_allowed:
        print(f"{method} is not valid. Please only enter allowed calculation method.")
        method = input(" | ".join(method_allowed) + ", Choose calculation method: ")

    repeat_second_prompt = True
    while repeat_second_prompt:
        second_operand = input("Enter operand: ")
        try:
            second_operand = int(second_operand)
            repeat_second_prompt = False
        except ValueError:
            print(f"{second_operand} is not a valid number.")

    if method == "+":
        answer = first_operand + second_operand
    elif method == "-":
        answer = first_operand - second_operand
    elif method == "*":
        answer = first_operand * second_operand
    elif method == "/":
        if second_operand == 0:
            print("Can't divide by 0")
        else:
            answer = first_operand / second_operand
    elif method == "%":
        if second_operand == 0:
            print("Can't divide by 0")
        else:
            answer = first_operand % second_operand
    elif method == "//":
        if second_operand == 0:
            print("Can't divide by 0")
        else:
            answer = first_operand // second_operand

    if answer is not None:
        print(f"Answer: {first_operand} {method} {second_operand} = {answer} \n")

    repeat_exit_prompt = True
    while repeat_exit_prompt:
        calculate_again = input("Would you like to do another calculation (y/n)? ")
        if calculate_again.lower() == "y":
            repeat_exit_prompt = False
        elif calculate_again.lower() == "n":
            print("Exiting program")
            running = False
            repeat_exit_prompt = False
        else:
            print("Wrong input. Only y/Y or n/N allowed") 
