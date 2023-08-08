import random
from .llm.prompts.promptCompiler import promptCompiler
from .llm.actions.call import conversation

def interaction(place):
    people = place.currentOccupancy
    if len(people) < 2: quit()

    interactors = []
    for person in people:
        roll = round(random.randint(1,3))
        if roll % 3 == 0: interactors.append(person)
    
    print(conversation(promptCompiler(interactors), "Fishing"))