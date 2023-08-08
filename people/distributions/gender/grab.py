import random
from .gender import genderDistribution

def grabGender():
    genders, weights = zip(*genderDistribution.items())
    gender = random.choices(genders, weights=weights)[0]
    return gender

