#This is the main program that will run
import time
from entity_functions import load_entities
from spacy.kb import KnowledgeBase
import spacy

print("Hi this is planet explorer!\n")
time.sleep(1)
question = input("What question would you like to ask?\n\n")

print(question)

print("Thank you!")

nlp = spacy.load("en_core_web_lg")
text = "Home is around yellow thing, near sad depressing planet."
doc = nlp(text)
for ent in doc.ents:
    print(f"Named Entity '{ent.text}' with label '{ent.label_}'")

name_dict, desc_dict = load_entities()
for QID in name_dict.keys():
    print(f"{QID}, name={name_dict[QID]}, desc={desc_dict[QID]}")

kb = KnowledgeBase(vocab=nlp.vocab, entity_vector_length=300)

for qid, desc in desc_dict.items():
    desc_doc = nlp(desc)
    desc_enc = desc_doc.vector
    kb.add_entity(entity=qid, entity_vector=desc_enc, freq=342)   # 342 is an arbitrary value here

for qid, name in name_dict.items():
    kb.add_alias(alias=name, entities=[qid], probabilities=[1])   # 100% prior probability P(entity|alias)

qids = name_dict.keys()
probs = [0.3 for qid in qids]
kb.add_alias(alias="Emerson", entities=qids, probabilities=probs)  # sum([probs]) should be <= 1 !

print(f"Entities in the KB: {kb.get_entity_strings()}")
print(f"Aliases in the KB: {kb.get_alias_strings()}")


print(f"Candidates for 'Earth': {[c.entity_ for c in kb.get_alias_candidates('home')]}")
print(f"Candidates for 'Sun': {[c.entity_ for c in kb.get_alias_candidates('yellow thing')]}")
print(f"Candidates for 'Pluto': {[c.entity_ for c in kb.get_alias_candidates('depressing')]}")

#https://medium.com/analytics-vidhya/nlp-text-encoding-a-beginners-guide-fa332d715854