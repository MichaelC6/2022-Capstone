#using NLTK library, we can do lot of text preprocesing
#This is useless at the moment.
import nltk
import time
nltk.download('punkt')
print("Hi this is planet explorer!\n")
time.sleep(1)
text = input("What question would you like to ask?\n\n")

#function to split text into word
tokens = nltk.tokenize.word_tokenize(text)
nltk.download('stopwords')
print(tokens)
print(text)

print("Thank you!")