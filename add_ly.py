word=input("Enter the string")
if word.endswith("ing"):
  word=word+"ly"
else:
  word=word+"ing"
print(word)
