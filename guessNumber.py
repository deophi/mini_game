import random
import speech_recognition as srec

def input_number():
    while True:
        answer  = input("Enter your answer (1-10): ")

        try:
            answer = int(answer)

            if(answer > 10):
                print("Answer number 1-10.\n")
                continue
            return answer
        except:
            print("Please answer number 1-10\n")

while True:
    print("Let's guess number between 1-10. You have 3 chances.\n")
    live = 3
    correct = random.randint(1, 10)

    while live > 0:
        answer = input_number()
        if (answer > correct):
            print("Your answer is too high.\n")
        elif (answer < correct):
            print("Your answer is too low.\n")
        else:
            print("Your answer is correct.\n")
            break

        live -= 1

    print("CONGRATULATION! You win the game." if live > 0 else "You lose.\n")
    
    while True:
        again = input("Do you want to play again? (y/n) ")

        if again == "y" or again == "n":
            break

    if again == "n":
        break

    print("Let's play again.\n\n")

print("The game is over.")