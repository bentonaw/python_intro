from random import randint, choice

# Generates list of numbers to iterate through for each math quiz
def generate_math_quiz_list(number_of_questions):
    quiz_list =[]

    max_repeat = 1
    if 14 <= number_of_questions <= 26:
        max_repeat = 2
    elif 27 <= number_of_questions <= 39:
        max_repeat = 3

    while len(quiz_list) < number_of_questions:
        random_int = randint(0,12)
        if quiz_list.count(random_int) < max_repeat:
            quiz_list.append(random_int)

    return quiz_list

# Generates list of doors according to number of questions
def generate_doors(nr_of_questions):
    list_of_doors = list(range(1, nr_of_questions + 1))
    return list_of_doors

# Assigns zombie door to a number witihin range of number of questions
def generate_zombie_door(doors_left):
    zombie_door = choice(list_of_doors)
    return zombie_door

# Function to create math quiz
def generate_math_quiz(math_operator, math_table, quiz_list, math_quiz_number):
    if math_operator == "*":
            math_quiz = math_table * quiz_list[math_quiz_number]
    elif math_operator == "//":
            math_quiz = quiz_list[math_quiz_number] // math_table
    elif math_operator == "%":
            math_quiz = quiz_list[math_quiz_number] % math_table

    return math_quiz

# Function to handle user string input
def input_valid_str(question, error_text, possible_answers):
    while True:
        answer = input(question)
        while answer not in possible_answers:
            answer = input(f'{error_text}\n{question}')

        return answer

# Function to handle user integer input    
def input_valid_int(question, error_text, min, max):
    while True:
        str = input(question)
        if str.isdigit() and min <= int(str) <= max:
            return int(str)
        print(error_text)
        
allowed_operators = ("*", "//", "%")
game_over_scenarios = ("You suddenly hear a door break down and see a swarm of zombies flooding the room! Game Over", "Crash! Zombies flood the room and charges towards you. Game Over", "You feel a hand on your shoulder and turn back. The last thing you see are a bunch of zombie teeth. Game Over")
game_over = False
reset_game = True

while not game_over:

    print("""\nOh no! You've found yourself trapped in a house with zombies!
        
There are multiple hallways with several doors to the way to the exit.
You hear the zombies behind one of the doors but cannot figure out which. 
The only way out is to solve a mathematical question and choose the right door to the zombies!
          """)

    while reset_game:
        nr_of_questions = input_valid_int("Choose number of math questions between 12-39 you would like to answer: ", "Input needs to be a number", 12, 39)
        math_operator = input_valid_str(f"Choose of which math operator you would like to answer ( {' | '.join(allowed_operators)} ): ", "Operator needs to be one of the allowed operators", allowed_operators)
        if math_operator == "*":
            math_table = input_valid_int("Which table between 2-12 would you like the questions in?: ", "Input needs to be a number between 2-12", 2, 12)
            break
        else:
            math_table = input_valid_int("Which divisor between 2-5 would you like the questions in?: ", "Input needs to be a number between 2-5", 2, 5)
            break
    
    # Generate list of doors, list of numbers for math quiz
    list_of_doors = generate_doors(nr_of_questions)
    smallest_number_on_door = min(int(i) for i in list_of_doors)
    largest_number_on_door = max(int(i) for i in list_of_doors)
    quiz_list = generate_math_quiz_list(nr_of_questions)
    reset_game = False

    print("\nTo be able to proceed you need to correctly answer each math quiz before choosing the correct door!")

    # Loop for answering math quizzes and choosing door
    math_quiz_number = 0
    while len(list_of_doors) >= 1 and not game_over:
        math_quiz = generate_math_quiz(math_operator, math_table, quiz_list, math_quiz_number)

        if len(list_of_doors) != 1:
            print(f"Question: {math_quiz_number + 1} out of {nr_of_questions}, {math_quiz_number} correctly answered quizzes so far")
            if math_operator == "*":
                answer = input_valid_int(f"What is {math_table} {math_operator} {quiz_list[math_quiz_number]}: ","Input should be a number", 0, 500)
            else:
                answer = input_valid_int(f"What is {quiz_list[math_quiz_number]} {math_operator} {math_table}: ","Input should be a number", 0, 500)
        else:
            if math_operator == "*":
                answer = input_valid_int(f"Final question! What is {math_table} {math_operator} {quiz_list[math_quiz_number]}: ","Input should be a number", 0, 500)
            else:
                answer = input_valid_int(f"Final question! What is {quiz_list[math_quiz_number]} {math_operator} {math_table}: ","Input should be a number", 0, 500)

        if answer != math_quiz:
            print(f"\nYou gueesed wrong, the correct answer is: {math_quiz}")
            print(game_over_scenarios[randint(0,2)])
            game_over = True
        else:
            math_quiz_number += 1
            print("\nCorrect!")

            if len(list_of_doors) == 1:
                print("You have made it! Congratulations! You have beaten the game!")
                reset_game = True
                break

            print(f"\nYou see {len(list_of_doors)} doors in front of you, which of the following would you like to open?")
            for door in list_of_doors:
                print(door, end="| "),
            
            while True:
                chosen_door = input_valid_int("Open door number: ", "Please enter a number from the line above.", smallest_number_on_door, largest_number_on_door)
                if chosen_door in list_of_doors:
                    zombie_door = generate_zombie_door(len(list_of_doors))
                    print(zombie_door)
                    if chosen_door != zombie_door:
                        print("\nWohoo! No zombies behind this door!")
                        print(f"The zombies were behind door nr {zombie_door}")
                        list_of_doors.remove(chosen_door)
                        break
                    else:
                        print(game_over_scenarios[randint(0,2)])
                        game_over = True
                        break
                else:
                    print("There is no door with that sign")
   
    while True:
        continue_game = input("\nWould you like to play again? (y/n)").lower()
        if continue_game == "y":
            game_over = False
            break
        elif continue_game == "n":
            print("thank you for playing. goodbye")
            game_over = True
            break
        else:
            print("Please enter either y or n")