def start_game():

    guesses = []
    correct_answers = 0
    question_number = 1

    for key in questions:
        print("********************")
        print(key)
        for i in answers[question_number - 1]:
            print(i)
        guess = input("Please enter your answer! Is it (A, B, C or D?): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_answers += check_answer(questions.get(key), guess)
        question_number += 1

    score_display(correct_answers, guesses)


def check_answer(answer, guess):

    if answer == guess:
        print("Well done! That's the correct answer :)")
        return 1
    else:
        print("Sorry, that's incorrect!")
        return 0


def score_display(correct_answers, guesses):
    print("***********************************")
    print("SCOREBOARD")
    print("***********************************")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_answers / len(questions)) * 100)
    print("Thanks for playing! Your score today is: " + str(score) + "%")


def start_over():
    pass


questions = {
    "What is the best selling console of all time?: ": "A",
    "Who are the creators of the well-known Final Fantasy series?: ": "C",
    "Who was the MAIN protagonist in Metal Gear Solid 2: Sons of Liberty?: ": "B",
    "What is the maximum score in the classic arcade game, 'Pac-man'?: ": "D",
    "What species of animal is Tom Nook?: ": "A",
    "What color is the 1-up mushroom in the Super Mario series?: ": "B",
    "What game popularized a new genre of game in 2011?: ": "C",
    "Which games company is the biggest host for simulated tycoon games?: ": "A",
    "Which one of these MMO's does Illidan Stormrage belong to?: ": "D",
    "Which mobile game blew up the gaming world in 2016?: ": "C"
}

answers = [
    ["A. Playstation 2", "B. Nintendo Switch",
        "C. Nintendo Wii", "D. Super Nintendo (SNES)"],
    ["A. Electronic Arts (EA)", "B. FROM Software",
     "C. Square Enix", "D. Blizzard"],
    ["A. Liquid Snake", "B. Raiden", "C. Big Boss", "D. Solidus"],
    ["A. 999,999,999", "B. 255", "C. 65,535", "D. 3,335,360"],
    ["A. Tanuki", "B. Raccoon", "C. Fox", "D. Badger"],
    ["A. Red", "B. Green", "C. White", "D. Blue"],
    ["A. The Elder Scrolls: Skyrim", "B. Dead Space 2", "C. Dark Souls", "D. Cars 2"],
    ["A. Frontier", "B. Introversion Software",
        "C. 2 point studios", "D. Paradox interactive"],
    ["A. Final Fantasy XIV", "B. Guild Wars",
        "C. Elder scrolls online", "D. World of Warcraft"],
    ["A. Candy Crush", "B. Angry Birds", "C. Pokemon GO", "D. Temple Run"],
]

start_game()
