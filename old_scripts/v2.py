#This is code I took from a variety of sources that I do not remember, this is not going to be used at the moment
#But want to keep it there for the process.
import nltk
from nltk.corpus import stopwords
import pandas as pd
from pathlib import Path
nltk.download('averaged_perceptron_tagger')
# first, define a function to preprocess the text by removing punctuation, stopwords, and lowercasing all words
def preprocess(text):
    text = text.lower() # lowercase all words
    tokens = nltk.word_tokenize(text) # tokenize the text into words
    stop_words = set(stopwords.words("english")) # get a list of stopwords in English
    filtered_tokens = [w for w in tokens if not w in stop_words] # remove stopwords
    return filtered_tokens

# next, define a function to extract the most important words from a question
def extract_important_words(question):
    # preprocess the question to remove punctuation, stopwords, etc.
    tokens = preprocess(question)

    # use NLTK to tag the preprocessed words with their part-of-speech
    tags = nltk.pos_tag(tokens)

    # create an empty list to hold the "important" words
    important_words = []

    # iterate through the tagged words and identify the "important" ones
    for word, pos in tags:
        if pos in ["NN", "NNP"]: # nouns and proper nouns are likely to be important
            important_words.append(word)
        elif pos in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]: # verbs are likely to indicate the action being taken
            important_words.append(word)

    # identify adjectives and adverbs, which often provide important information
    if pos in ["JJ", "JJR", "JJS", "RB", "RBR", "RBS"]:
        important_words.append(word)

    # identify prepositions and determiners, which often indicate the context of the sentence
    if pos in ["IN", "DT"]:
        important_words.append(word)

    # return the list of important words
    return important_words

# now, let's test our function on some sample questions
question = input("What is your question?\n")

important_words = extract_important_words(question)

# print the question and the important words
print("Question:", question)
print("Important words:", important_words)

df = pd.read_csv("../assets/planets.csv")
print(df)