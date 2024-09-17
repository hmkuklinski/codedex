from textblob import TextBlob

#text with spelling error:
text = "I love programming and machine learnig"

#create a textblob object w/ text:
blob = TextBlob(text)

#check the spelling:
corrected_text = blob.correct()
print("Original text: ", text)
print("Corrected text: ", corrected_text)