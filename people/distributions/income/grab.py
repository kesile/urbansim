import random
from .income import incomeDistribution

def grabIncome(age):
    income = random.gauss(incomeDistribution["mu"], incomeDistribution["sigma"])

    if income < incomeDistribution["lowerBound"]: income = incomeDistribution["lowerBound"]
    if income > incomeDistribution["upperBound"]: income = incomeDistribution["upperBound"]
    
    if age <= 14:
        income = income * incomeDistribution["penaltyKid"]
    if age <= 18:
        income = income * incomeDistribution["penaltyTeen"]
    else: 
        income = income * incomeDistribution["penaltyAdult"]

    income = round(income, 0)

    return income