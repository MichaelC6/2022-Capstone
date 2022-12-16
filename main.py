#This is the main program that will run
import time
import pandas
import pandas as pd
import numpy as np
from nlp import extract_important_words
from fuzzywuzzy import fuzz
import spacy
import en_core_web_lg

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
planet = ""
for cPlanet in planets:
    if cPlanet in important_words:
        planet = cPlanet

features = df.columns.values.tolist()

#print(features)

important_words.remove(planet)
nlp = spacy.load("en_core_web_lg")

feature_score = []
for feature in features:
    word_score = []
    for word in important_words:
        doc1 = nlp(word)
        doc2 = nlp(feature)
        word_score.append(doc1.similarity(doc2))
        #word_score.append(fuzz.ratio(word.lower(), feature.lower()))
    word_score = np.array(word_score)
    feature_score.append(word_score.max())
max_feature = np.argmax(feature_score)

#print(feature_score)
print("Your question was:")
#print(question)
print(f"The feature this most matches is {features[max_feature]}.")