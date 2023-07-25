import random

while True:
    print("Let's guess number between 1-10. You have 3 chances.\n")
    live = 3
    correct = random.randint(1, 10)

    def input_number():
        while True:
            answer  = input("Input your number: ")

            try:
                answer = int(answer)

                if(answer > 10):
                    print("Enter number 1-10.\n")
                    continue
                return answer
            except:
                print("Please enter number 1-10\n")

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