def findSchedule(weekday, weekend, runTime):
    while runTime > 168: runTime =- 168

    if runTime <= 120:
        return weekday
    else: 
        return weekend
    