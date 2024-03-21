from pathlib import Path
import sys
import os

def assign_points(entry,letters):
    word = entry.lower()
    score = 0
    for letter in letters:
        if(letter in word):
            file_name = letter+"_f"
            file = file_name+".txt"

            here = Path(__file__).resolve()
            root_folder = here.parents[0]
            name = "letter_files/"+file
            my_path = root_folder / name
  
            with open(my_path,'r') as f:
                if(word in f.read()):
                    score+=10
            f.close()
    return score