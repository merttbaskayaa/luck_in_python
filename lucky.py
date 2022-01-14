import random

def chance(chance_percentage):
    random_number = random.randint(0, 100)
    if chance_percentage >= random_number:
        print("WİN")
    else:
        print("LOSE")
