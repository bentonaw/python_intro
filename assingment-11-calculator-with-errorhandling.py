# Splits input into seperate values into a list
def extract_operands(input): 
    operands = input.split()
    operands = [str(e) for e in operands]
    return operands

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


while True:
    correct_input = False
    while not correct_input:
        user_input = input("What would you like to calculate?: ")
        operands = extract_operands(user_input)
        try:
            first_operand = float(operands[0])
            second_operand = float(operands[2])
            method = operands[1]
            calculate(method)
            correct_input = True
        except ValueError:
            print("Wrong input, only enter digits \n")
        except ZeroDivisionError:
            print("Can't divide by zero! \n")
        except UnboundLocalError:
            print("Unknown operator! \n")
        except:
            print("Missing operand or operator! \n")

    if calculate(method) is not None:
        print(f"{first_operand} {method} {second_operand} = {calculate(method)} \n")
