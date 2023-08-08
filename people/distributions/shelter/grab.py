import random
from .shelter import shelterDistribution

def grabShelter():
    shelters, weights = zip(*shelterDistribution.items())
    shelter = random.choices(shelters, weights=weights)[0]
    return shelter