import random
import time
from questions import quiz_data

# Color Design
try:
    from colorama import Fore, Style, init
    init()

except:
    class Fore:
        GREEN = ""
        RED = ""
        CYAN = ""
        YELLOW = ""

    class Style:
        RESET_ALL = ""



# Welcome UI
print(Fore.CYAN + "=" * 65)
print("                 SMART AI QUIZ GENERATOR")
print("=" * 65 + Style.RESET_ALL)

name = input("\nEnter Your Name: ")

print(Fore.YELLOW + f"\nWelcome {name}!" + Style.RESET_ALL)

# Category Selection
print("\nSelect Category")
print("1. Python")
print("2. GK")

category_choice = input("\nEnter choice: ")

if category_choice == "1":
    category = "Python"

elif category_choice == "2":
    category = "GK"

else:
    print("\nInvalid choice! Defaulting to Python")
    category = "Python"



# Difficulty Selection
print("\nSelect Difficulty")
print("1. Easy")
print("2. Hard")

difficulty_choice = input("\nEnter choice: ")

if difficulty_choice == "1":
    difficulty = "Easy"

elif difficulty_choice == "2":
    difficulty = "Hard"

else:
    print("\nInvalid choice! Defaulting to Easy")
    difficulty = "Easy"



# Fetch Questions
questions = quiz_data[category][difficulty]

# Shuffle Questions
random.shuffle(questions)

score = 0
question_no = 1
total_time = 0

motivations = [
    "Keep Learning!",
    "Never Give Up!",
    "Practice Makes Perfect!",
    "Success Comes With Consistency!",
    "Coding Is Fun!"
]

print(Fore.CYAN + f"\nStarting {difficulty} Quiz..." + Style.RESET_ALL)

time.sleep(2)

# Quiz Loop
for q in questions:

    print("\n" + "-" * 65)
    print(f"Question {question_no}")
    print("-" * 65)

    print(q["question"])

    print()

    for option in q["options"]:
        print(option)

    # Timer Start
    start = time.time()

    user_answer = input("\nEnter Answer (A/B/C/D): ").upper()

    # Timer End
    end = time.time()

    taken = int(end - start)

    total_time += taken

    print(f"\nTime Taken: {taken} seconds")

    # Answer Checking
    if user_answer == q["answer"]:

        print(Fore.GREEN + "Correct Answer!" + Style.RESET_ALL)

        score += 1

    else:

        print(Fore.RED + "Wrong Answer!" + Style.RESET_ALL)

        print("Correct Answer is:", q["answer"])

        # Negative Mark
        score -= 0.5

    question_no += 1

    time.sleep(1)


# Final Result
print(Fore.CYAN + "\n" + "=" * 65)
print("                     QUIZ COMPLETED")
print("=" * 65 + Style.RESET_ALL)

print(f"\nPlayer Name : {name}")
print(f"Category    : {category}")
print(f"Difficulty  : {difficulty}")
print(f"Final Score : {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

print(f"Percentage  : {percentage}%")
print(f"Total Time  : {total_time} seconds")


# AI Analysis
print(Fore.YELLOW + "\nAI PERFORMANCE ANALYSIS")
print("-" * 65 + Style.RESET_ALL)

if percentage >= 90:

    print(Fore.GREEN + "Outstanding Performance!" + Style.RESET_ALL)
    print("AI detected excellent knowledge level.")

elif percentage >= 70:

    print(Fore.GREEN + "Very Good Performance!" + Style.RESET_ALL)
    print("AI detected strong understanding.")

elif percentage >= 40:

    print(Fore.YELLOW + "Average Performance!" + Style.RESET_ALL)
    print("AI suggests more practice.")

else:

    print(Fore.RED + "Poor Performance!" + Style.RESET_ALL)
    print("AI recommends improvement.")



# Grade System
print(Fore.CYAN + "\nGRADE REPORT")
print("-" * 65 + Style.RESET_ALL)

if percentage >= 90:
    grade = "A+"

elif percentage >= 75:
    grade = "A"

elif percentage >= 60:
    grade = "B"

elif percentage >= 40:
    grade = "C"

else:
    grade = "FAIL"

print("Your Grade:", grade)


# Motivation Quote
print(Fore.YELLOW + "\nMOTIVATIONAL QUOTE")
print("-" * 65 + Style.RESET_ALL)

print(random.choice(motivations))


# Save Leaderboard
with open("leaderboard.txt", "a") as file:

    file.write(
        f"{name} | {category} | {difficulty} | "
        f"Score: {score} | Percentage: {percentage}%\n"
    )


# View Leaderboard
print(Fore.CYAN + "\nLEADERBOARD")
print("-" * 65 + Style.RESET_ALL)

try:

    with open("leaderboard.txt", "r") as file:

        data = file.readlines()

        for line in data[-5:]:
            print(line)

except:

    print("No leaderboard data found.")


# Replay Option
again = input("\nDo you want to play again? (yes/no): ").lower()

if again == "yes":

    print("\nRestart the program.")

else:

    print(Fore.GREEN + "\nThank You For Using Smart AI Quiz Generator!" + Style.RESET_ALL)