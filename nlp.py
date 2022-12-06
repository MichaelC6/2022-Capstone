#This python file deals with the NLP around my project.
import nltk
from nltk.corpus import stopwords
nltk.download('maxent_ne_chunker')
nltk.download('words')

# first, define a function to preprocess the text by removing punctuation, stopwords, and lowercasing all words
def preprocess(text):
    text = text.lower() # lowercase all words
    tokens = nltk.word_tokenize(text) # tokenize the text into words
    stop_words = set(stopwords.words("english")) # get a list of stopwords in English
    filtered_tokens = [w for w in tokens if not w in stop_words] # remove stopwords
    return filtered_tokens

# next, define a function to extract the most important words from a question using named entity recognition
def extract_important_words(question):
    # preprocess the question to remove punctuation, stopwords, etc.
    tokens = preprocess(question)

    # use NLTK to tag the preprocessed words with their part-of-speech
    tags = nltk.pos_tag(tokens)

    # create an empty list to hold the "important" words
    important_words = []

    # iterate through the tagged words and identify the "important" ones
    for word, pos in tags:
        if pos in ["NN", "NNP", "JJ", "RB"]: # nouns and proper nouns are likely to be important
            important_words.append(word)
        elif pos in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]: # verbs are likely to indicate the action being taken
            important_words.append(word)

    # return the list of important words
    return important_words

