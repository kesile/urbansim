from people.person import createPerson
from buildings.building import Building, locations

from people.llm.calls.broadText import textCall
from people.llm.calls.narrowText import narrowText

from people.llm.prompts.broadSchedule.functions.schedule import functions
from people.llm.prompts.broadSchedule.instructions.weekdaySchedules import weekdayScheduleInstructions

from people.llm.prompts.narrowSchedule.functions.functions import createNarrow
from people.llm.prompts.narrowSchedule.prompts.narrowPrompt import narrowPrompt
import staticDB.methodAggregation as data

import os, json, pickle
from interactions.handler import interaction

from clock.time import Time

time = Time()

os.system("clear")

people = { }
for i in range(10):
    people.update({i : createPerson(i)})

path = data.getPath()

data.pushData(people, path)

people = data.pullData(path)
