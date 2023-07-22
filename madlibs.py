with open("story.txt", "r") as f:
    story = f.read()

words       = set()
wordStart   = -1
targetStart = "<"
targetEnd   = ">"

for i, char in enumerate(story):
    if char == targetStart:
        wordStart = i
    
    if char == targetEnd and targetStart != -1:
        word = story[wordStart : i+1]
        words.add(word)
        wordStart = -1

answers = {}

for word in words:
    answer = input("Enter a word for" + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)