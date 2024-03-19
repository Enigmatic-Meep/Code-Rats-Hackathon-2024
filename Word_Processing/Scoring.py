from pathlib import Path

def assign_points(entry,letters):
    data_folder = Path("letter_files/")
    word = entry.lower()
    score = 0
    for letter in letters:
        if(letter in word):
            file_name = letter+"_f.txt"
            file = data_folder / file_name
            f = open(file,"r")
            if(word in f.read()):
                score+=1
            f.close()
    return score
