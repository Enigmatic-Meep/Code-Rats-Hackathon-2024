import random

def generate_letters():
    generated = []
    letters  = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(0,4):
        index=random.randint(0,len(letters)-1)
        generated.append(letters[index])
        letters.pop(index)
    return generated
