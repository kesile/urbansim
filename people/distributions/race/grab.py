import random
from .race import raceDistribution

def grabRace():
    races, weights = zip(*raceDistribution.items())
    race = random.choices(races, weights=weights)[0]
    return race