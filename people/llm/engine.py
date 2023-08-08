from calls.broadText import broadText

def makeSchedule(type):
    match type:
        case "weekday":
            broadScheduler(type)

scheduleGeneral = broadText(persn)