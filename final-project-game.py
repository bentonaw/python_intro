from random import randint

# Generates list of numbers to iterate through for each math quiz
def generate_math_quiz_list(number_of_questions):
    quiz_list =[]

    if 13 >= number_of_questions:
        while len(quiz_list) < number_of_questions:
            random_int = randint(0,12)
            if random_int not in quiz_list:
                quiz_list.append(random_int)
    elif 14 <= number_of_questions <= 26:
        while len(quiz_list) < number_of_questions:
            random_int = randint(0,12)
            if quiz_list.count(random_int) < 2:
                quiz_list.append(random_int)
    elif 27 <= number_of_questions <= 39:
        while len(quiz_list) < number_of_questions:
            random_int = randint(0,12)
            if quiz_list.count(random_int) < 3:
                quiz_list.append(random_int)

    return quiz_list

# Generates list of doors according to number of questions
def generate_doors(nr_of_questions):
    list_of_doors = []
    door = 0
    while len(list_of_doors) < nr_of_questions:
        door += 1
        list_of_doors.append(door)
    return list_of_doors

# Assigns zombie door to a number witihin range of number of questions
def generate_zombie_door(doors_left):
    zombie_door = randint(1,doors_left)
    return zombie_door

# Function to create math quiz
def generate_math_quiz(math_operator, math_table, quiz_list, math_quiz_number):
    if math_operator == "*":
            math_quiz = math_table * quiz_list[math_quiz_number]
    elif math_operator == "/":
            math_quiz = int(quiz_list[math_quiz_number] / math_table)
    elif math_operator == "%":
            math_quiz = quiz_list[math_quiz_number] % math_table
    
    return math_quiz

# Function to error handle non integer input
def handle_integer_input(prompt, error_message):
    while True:
        try:
            allowed_number = int(input(prompt))
            return allowed_number
        except:
            print(error_message)

        

game_over_scenarios = ("You suddenly hear a door break down and see a swarm of zombies flooding the room! Game Over", "Crash! Zombies flood the room and charges towards you. Game Over", "You feel a hand on your shoulder and turn back. The last thing you see are a bunch of zombie teeth. Game Over")
game_over = False
reset_game = True

while not game_over:

    print("""\nOh no! You've found yourself trapped in a house with zombies!
        
There are multiple hallways with several doors to the way to the exit.
You hear the zombies behind one of the doors but cannot figure out which. 
The only way out is to solve a mathematical question and choose the right door to the zombies!
          """)

    # number needs to be between 12-39
    while reset_game:
        nr_of_questions = handle_integer_input("Choose number of math questions between 12-39 you would like to answer: ","Input needs to be a number")
        if 12 <= nr_of_questions <= 39:
            break
        else:
            print("Number needs to be between 12-39")

    # user inputs whcih operator to use with only allowing *, /, %
    while True and reset_game:
        try:
            math_operator = input("Choose of which math operator you would like to answer ( * | / | % ): ")
            if math_operator in ["*","%"]:
                break
            elif math_operator == "/":
                print("Answers will be the integer without any decimals")
                break
            else:
                print("Operator needs to be either *,/ or %")
        except:
            print("Incorrect input, only input either *,/ or %")

    # user inputs which math table to use 
    while reset_game:
        if math_operator == "*":
            math_table = handle_integer_input("Which table between 2-12 would you like the questions in?: ", "Input needs to be a number")
            if 2 <= math_table <= 12:
                break
            else:
                print("Number needs to be between 2-12")
        else:
            math_table = handle_integer_input("Which table between 2-5 would you like the questions in?: ", "Input needs to be a number")
            if 2 <= math_table <= 5:
                break
            else:
                print("Number needs to be between 2-5")

    # Generate list of doors, list of numbers for math quiz and a door number for zombie quiz
    list_of_doors = generate_doors(nr_of_questions)
    quiz_list = generate_math_quiz_list(nr_of_questions)
    zombie_door = generate_zombie_door(len(list_of_doors))
    reset_game = False

    print("\nTo be able to proceed you need to correctly answer each math quiz before choosing the correct door!")

    # Loop for answering math quizzes and choosing door
    math_quiz_number = 0
    while len(list_of_doors) > 1 and not game_over:
        math_quiz = generate_math_quiz(math_operator, math_table, quiz_list, math_quiz_number)

        if len(list_of_doors) != 1:
            print(f"Question: {math_quiz_number + 1} out of {nr_of_questions}, {math_quiz_number} correctly answered quizzes so far")
            if math_operator == "*":
                answer = handle_integer_input(f"What is {math_table} {math_operator} {quiz_list[math_quiz_number]}: ","Input should be a number")
            else:
                answer = handle_integer_input(f"What is {quiz_list[math_quiz_number]} {math_operator} {math_table}: ","Input should be a number")
        else:
            if math_operator == "*":
                answer = handle_integer_input(f"Final question! What is {math_table} {math_operator} {quiz_list[math_quiz_number]}: ","Input should be a number")
            else:
                answer = handle_integer_input(f"Final question! What is {quiz_list[math_quiz_number]} {math_operator} {math_table}: ","Input should be a number")

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
            
            chosen_door = handle_integer_input("Open door number: ", "There is no door with that sign")
            if chosen_door != zombie_door:
                print("\nWohoo! No zombies behind this door!")
                print(f"The zombies were behind door nr {zombie_door}")
                list_of_doors.remove(chosen_door)
                zombie_door = generate_zombie_door(len(list_of_doors))
                while zombie_door not in list_of_doors:
                    zombie_door = randint(1,len(list_of_doors))
            else:
                print(game_over_scenarios[randint(0,2)])
                game_over = True
   
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
            continue