import random

def roll():
    minValue = 1
    maxValue = 6
    return random.randint(minValue, maxValue)

def sortPlayerPosition(array):
    for i in range(players-1):
        for j in range(players-1):
            if array[j][1] <= maxScore and array[j+1][1] <= maxScore and array[j][1] < array[j+1][1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            elif array[j][1] > 20 and array[j+1][1] <= maxScore and array[j][1] < array[j+1][1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

print("Input total players (min. 2 players) and max score. Every time the dice is thrown, it will accumulate to your score. If your score get higher than max score, you will eliminated in this game.")
print("\nLet's Start The Game!\n")

while True:
    maxScore = input("Enter max score for this game: ")
    if maxScore.isdigit():
        maxScore = int(maxScore)
        break

    print("input must be numeric.")

while True:
    players = input("Enter the number of players: ")

    if players.isdigit():
        players = int(players)

        if players > 1:
            break
        
        print("Total players must be more than 2!")
        continue

    print("Input must be number.")

print("Total players is", str(players) + ". Let's Play!\n")

playersScore = [[0 for i in range(2)] for j in range(players)]

for i in range(players):
    print("Player", i+1, "turn.")
    playersScore[i][0] = input("Write your name: ")
    while playersScore[i][1] < maxScore:
        doRoll = input("Do you want to roll? (y/n) ").lower()

        if doRoll != "y" and doRoll != "n":
            print("Input must be (y/n)\n")
            continue

        if doRoll == "n":
            print("Your total score is", playersScore[i][1])
            break

        scrollValue = roll()
        playersScore[i][1] += scrollValue
        print("Your dice is", scrollValue)
        print("Your total score is", playersScore[i][1], "\n")

        if playersScore[i][1] == maxScore:
            print("Congratulation!", playersScore[i][0], "WIN the GAME!")
            break
        elif playersScore[i][1] > maxScore:
            print("Your score is higher than", str(maxScore) + ". You are eliminated!")
            continue
    
    if playersScore[i][1] == maxScore:
        break
    
    print(playersScore[i][0], "score is", playersScore[i][1],"\n")

sortPlayerPosition(playersScore)

for i in range(players):
    if playersScore[i][1] > maxScore:
        print(playersScore[i][0], "eliminated.")
    else:
        print(playersScore[i][0], "score is", playersScore[i][1])

print("\nGame Ends...")