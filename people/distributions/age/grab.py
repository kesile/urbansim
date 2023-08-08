import random
from .age import ageDistribution

def grabAge():
    age = random.gauss(ageDistribution["mu"], ageDistribution["sigma"])
    if age < ageDistribution["lowerBound"]: age = ageDistribution["lowerBound"]
    if age > ageDistribution["upperBound"]: age = ageDistribution["upperBound"]
    return age

