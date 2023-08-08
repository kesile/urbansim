import random
from .transportation import transportationDistribution

def grabTransportation():
    transportations, weights = zip(*transportationDistribution.items())
    transportation = random.choices(transportations, weights=weights)[0]
    return transportation