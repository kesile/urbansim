import random
from .jobs import jobDistribution

def grabJob(age):
    if age > 18:
        jobs, weights = zip(*jobDistribution.items())
        randJob = random.choices(jobs, weights=weights)[0]
    else: randJob = "Student"
    return randJob