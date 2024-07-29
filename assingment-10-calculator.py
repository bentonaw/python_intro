# Splits input into seperate values into a list
def extract_operands(input): 
    operands = input.split()
    operands = [str(e) for e in operands]
    return operands

# If calculation method is not in Tuple of methods allowed return true
def is_method_allowed(method, method_allowed):
    return method in method_allowed
    
# If divided by zero is tried return True
def tried_zero_division(method, second_operand):
    return method in ("/", "%", "//") and second_operand == 0

# Calculates answer 
def calculate(method):
    if method == "+":
        answer = first_operand + second_operand
    elif method == "-":
        answer = first_operand - second_operand
    elif method == "*":
        answer = first_operand * second_operand
    elif method == "/":
        answer = first_operand / second_operand
    elif method == "%":
        answer = first_operand % second_operand
    elif method == "//":
        answer = first_operand // second_operand
    return answer


method_allowed = ("+", "-", "*", "/", "%", "//")

while True:
    user_input = input("What would you like to calculate?: ")
    operands = extract_operands(user_input)
    first_operand = float(operands[0])
    method = operands[1]
    second_operand = float(operands[2])

    #  Function calculate will not unless method is not allowed or zero division is tried
    if not is_method_allowed(method, method_allowed):
        print("Unknown operator!")
    elif tried_zero_division(method, second_operand):
        print("Can't divide by zero!")
    elif calculate(method) is not None:
        print(f"{first_operand} {method} {second_operand} = {calculate(method)} \n")


