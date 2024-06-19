import random
from random import randint


    # Asks user how many rounds they would like to do.
def quiz_rounds():
    while True:
        try:
            rounds = int(input("How many questions would you like to answer?:"))
            Score = 0
            Incorrect = 0
            quiz_list = []
            if rounds >= 1:
                for x in range(rounds):
                    num1 = random.randint(1, 100)
                    num2 = random.randint(1, 100)
                    correct_answer = num1 + num2
            
                    print(f"\nQuestion {x + 1}:")
                    while True:
                        try:
                            print(f"What is {num1} + {num2}?\n")
                            user_answer = int(input("Your answer: "))
                            break
                        except ValueError: 
                            print("Invalid input, please enter a number\n")
                    if user_answer == correct_answer:
                        print("Correct!")
                        Score += 1
                        quiz_list.append(f"{x + 1}: {num1}+{num2} = {correct_answer}, you put: {user_answer}") 
                        
                    else:
                        print(f"Incorrect. The correct answer is {correct_answer}.")
                        quiz_list.append(f"{x + 1}: {num1}+{num2} = {correct_answer}, you put: {user_answer}") 
                    
            print(f"\nTest completed!\n\nYou scored: {Score}/{rounds}")
            history(quiz_list, name, rounds, Score)                        

                        
        except ValueError: 
             print("Invalid input, please enter a number\n")
        

# Function showing Quiz History
def history(quiz_list, name, rounds, Score):  # Pass 'name' and 'quiz_list' as an argument
    # Calculate the percentage of correct answers
    
    winrate = (Score / rounds) * 100
    print('You have a win rate of: {:.2f}%'.format(winrate))
    
    
    while True:
        history = input(f"Would you like to see your Quiz History, "
                       f"so you can see what you got right {name}?\n\n"
                       f"Type Yes or No.\n")
        if history in ["Yes", "yes"]:
            print(f"Here is your Quiz History {name}:\n")
            print(*quiz_list, sep="\n")
            print("\n^^These are the results.^^\n\n")
            break  # Exit the loop after displaying history
        elif history in ["No", "no"]:
            print("Okay, no problem!")
            break  # Exit the loop if user says 'no'
        else:
            print("That wasn't an option, please select Yes or No.") 

    # Asks user if they want to Replay 
    while True: 
            replay = input("Would you like to Replay the Quiz?\n\n") 
            if replay in ["Yes", "yes"]: 
                quiz_rounds() 
                break
            elif replay in ["No", "no"]: 
                print("Okay, thanks for playing!")
                quit()

    # Title / Asks for users name
print("**Welcome to the Math Quiz!**\n")
name = input("Please enter your name.\n")
print(f"Nice to meet you {name}.\n") 
print("You will be asked as many questions as you like, and once finished, you will be able to review your results and replay the quiz if you wish, Good Luck!\n")
quiz_list = []
Score = 0
Incorrect = 0
quiz_rounds()
history(quiz_list, name, quiz_rounds, Score)
