from translate import Translator

#create translator object:
translator = Translator(to_lang="ko")

#choose text to translate and print translation:
text= "I love Stray Kids"
translation = translator.translate(text)
print(translation)