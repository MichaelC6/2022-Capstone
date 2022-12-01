#This is code to load entities
#This code is taken from https://github.com/explosion/projects/blob/master/nel-emerson/scripts/notebook_video.ipynb
import csv
from pathlib import Path

def load_entities():
    entities_loc = Path.cwd().parent / "input" / "entities.csv"  # distributed alongside this notebook

    names = dict()
    descriptions = dict()
    with entities_loc.open("r", encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        for row in csvreader:
            qid = row[0]
            name = row[1]
            desc = row[2]
            names[qid] = name
            descriptions[qid] = desc
    return names, descriptions