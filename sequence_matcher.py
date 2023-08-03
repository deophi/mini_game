from difflib import SequenceMatcher
text1 = "The One Piece is Real"
text2 = "I want to be Pirates King"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {round(sequenceScore*100, 2)} % similar")