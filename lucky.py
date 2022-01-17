import random

def chance(chance_percentage):
    random_number = random.randint(0, 100)
    if chance_percentage >= random_number:
        return True
    else:
        return False
    
print(chance(50))

# With a 50 percent chance, the software returns a value to us. True so you win or False you lose.
