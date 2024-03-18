from pathlib import Path

data_folder = Path("code/text_files/")
file_to_open = data_folder / "raw_data.txt"

def assign_points(entry,letters):
    word = entry.lower()
    score = 0
    for letter in letters:
        if(letter in word):
            file = letter+"_f.txt"
            f = open(file,"r")
            if(word in f.read()):
                score+=1
            f.close()
    return score

print(assign_points("apple",["a","p","l"]))