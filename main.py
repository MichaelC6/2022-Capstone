#This is the main program that will run
import time
import pandas
import pandas as pd

from nlp import extract_important_words

print("Hi this is planet explorer!\n")
time.sleep(1)
question = input("What question would you like to ask?\n\n")

print(question)

print("Thank you!")


important_words = extract_important_words(question)

print(important_words)


df = pd.read_csv("assets/planets.csv")

planets = df["Planet"].tolist()
planets = [planet.lower() for planet in planets]

#need to match planet


