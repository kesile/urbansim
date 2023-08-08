def updateSchedule(schedule, time, category, desc):
    schedule[time][category] = desc
    return schedule