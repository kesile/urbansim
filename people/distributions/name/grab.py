import requests as re
import random
from .names import maleNames, femaleNames
def grabName(gender):
    gender = gender.lower()

    if gender == "man":
        return random.choice(maleNames)
    if gender == "woman":
        return random.choice(femaleNames)
    else:
        return random.choice(maleNames + femaleNames)

