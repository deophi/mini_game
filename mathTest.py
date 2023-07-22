import random

minValue  = 1
maxValue  = 10
operators = ["+", "-", "*", "/"]
correct   = 0
i         = 0

def generateQuestion():
    firstValue  = random.randint(minValue, maxValue)
    secondValue = random.randint(minValue, maxValue)
    operator    = random.choice(operators)

    question = str(firstValue)+" "+operator+" "+str(secondValue)
    answer   = float(eval(question))

    while True:
        guess = input(question+" = ")

        # if guess.isnumeric():
        #     guess = int(guess)
        #     break
        try:
            guess = float(guess)
            break
        except:
            continue

    if "%.2f" % guess == "%.2f" % answer:
        print("Congratulation! Your answer is correct")
        return 1
    else:
        print("The correct answer is", "%.2f" % answer)
        return 0

print("Let's start the test!\n")

while True:
    do = input("Do you want to continue question number "+ str(int(i)+1) +"? (y/n) ").lower()

    if do != "y" and do != "n":
        print("input must be (y/n)")
        continue

    if do == "n":
        break

    print("\nQuestion number", i+1)
    correct += generateQuestion()
    i += 1

if correct == 0:
    print("You never ask any questions.")
elif correct == i:
    print("CONGRATULATION!")
    print("You have answered all questions perfectly!")
else:
    print("You have answered", correct, "of", i, "questions.")
    print("Your score is "+ str((correct/i)*100))
    print("Hope you will be better next time.")