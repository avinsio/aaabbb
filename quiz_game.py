print("Welcome to the Quiz Game!")
playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

def ask_question(question, correct_answer):
    answer = input(question + " ").strip().lower()

    if answer == correct_answer.strip().lower():
        print("Correct!")
        return 1 
    else:
        print(f"Incorrect! The answer is {correct_answer}")
        return 0
    
questions = {
    "How many hearts does an octopus have?": "3",
    "Which planet is the hottest?": "venus",
    "How many months have 28 days?": "12",
    "What gets wetter the more it dries?": "towel",
    "Which animal has cube-shaped poop?": "wombat",
    "What is the fastest land animal?": "cheetah",
    "Which planet has the Great Red Spot?": "jupiter",
    "What has hands but cannot clap?": "clock",
    "How many bones are in a typical adult human body?": "206",
    "What is the name of Mario's brother?": "luigi"
}

for question, answer in questions.items():
    score += ask_question(question, answer)

print("Your total score:", score)






