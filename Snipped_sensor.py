
#Snipped simple word sensor

def word_censor(text, word):
    if word in text:
      text= text.replace(word, "*" *len(word))
    print(text)
    return text
    
word_censor("Hola Fuck", "Fuck")
