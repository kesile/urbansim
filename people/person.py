from .methods.findSchedule import findSchedule
from .methods.move import move
from .methods.updateSchedule import updateSchedule
from .methods.getAssets import getAssets
from .distributions import dist

class Person():
    def __init__(self, identity, name, age, gender, race, location, transportation, income, assets, job, shelter, personality):
        self.identity, self.name, self.age, self.gender, self.race, self.location, self.transportation, self.income, self.assets, self.job, self.shelter, self.personality = identity, name, age, gender, race, location, transportation, income, assets, job, shelter, personality
        self.assets = self._getAssets(self.transportation, self.shelter)
    
    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}, Gender: {self.gender}, Race: {self.race}, Location: {self.location}, Transportation: {self.transportation}, Income: {self.income}, Assets: {self.assets}, Job: {self.job}, Shelter: {self.shelter} \n Description: {self.personality}"

    def _findSchedule(self, weekday, weekend, runTime):
        return findSchedule(weekday, weekend, runTime)
    
    def _move(self, place):
        self.location = place
    
    def _updateSchedule(self, schedule, time, category, desc):
        schedule = updateSchedule(schedule, time, category, desc)

    def _getAssets(self, transportation, shelter):
        assets = getAssets(transportation, shelter)
        return assets

def createPerson(identity):
    identity = identity
    age = round(dist.grabAge(),0)
    gender = dist.grabGender()
    name = dist.grabName(gender)
    race = dist.grabRace()
    location = "N/A"
    transportation = dist.grabTransportation()
    income = dist.grabIncome(age)
    assets = "N/A"
    job = dist.grabJob(age)
    shelter = dist.grabShelter()
    personality = dist.grabPersonality(name)

    human = Person(identity, name, age, gender, race, location, transportation, income, assets, job, shelter, personality)
    return human
