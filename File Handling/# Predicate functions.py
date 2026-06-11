# Predicate functions

def Human(x):
    return x in ["Socrates", "Plato"]

def Mortal(x):
    return Human(x)   # Rule: Human(x) → Mortal(x)

# Query
print("Is Socrates Mortal?", Mortal("Socrates"))