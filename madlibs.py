while True:
    lang = input("Which story do you want? (ENG/IDN) ").upper()
    story = ""
    if lang == "ENG":
        story = "english_story"
        break
    elif lang == "IDN":
        story = "indonesian_story"
        break
    print("Input must be \"IDN\" or \"ENG\"!")
    
with open(story+".txt", "r") as f:
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

print("\n"+story)