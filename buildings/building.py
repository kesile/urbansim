locations = []

class Building:
    def __init__(self, name, address, floors, capacity):
        self.name = name
        self.address = address
        self.floors = floors
        self.capacity = capacity
        self.currentOccupancy = []
        locations.append(self)

    def addOccupant(self, person):
        person._move(self.name)
        self.currentOccupancy.append(person)
    
    def removeOccupant(self, person):
        if person in self.currentOccupancy:
            self.currentOccupancy.remove(person)
            person._move("Outdoors")
        else:
            print("error: no such person in building")

    def getAvailableSpace(self):
        return self.capacity - self.currentOccupancy

    def __str__(self):
        return f"{self.name}, located at {self.address}, has {self.floors} floors and a capacity of {self.capacity} occupants. Current occupancy: {self.currentOccupancy}"
