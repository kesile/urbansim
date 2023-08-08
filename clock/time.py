class Time:
    def __init__(self):
        self.time = "0:00"
        self.runTime = 0
        self.simTime = 0

    def _timeToString(self, time):
        hour = time // 60
        minute = time % 60
        hour = str(hour)
        if minute < 10:
            minute = f"0{str(minute)}"
        else:
            minute = str(minute)
        return f"{hour}:{minute}"

    def _timeCheck(self):
        if self.simTime == 24 * 60:
            self.simTime = 0
        return self.simTime
    
    def _date(self):
        time = self.runTime
        month = ""

    def _stepForward(self):
        self.runTime += 5
        self.simTime += 5
        self.simTime = self._timeCheck()
        self.time = self._timeToString(self.simTime)
        print("\nTime Moved Forward By 5 Minutes\n")
        return self.simTime, self.runTime, self.time

    def __str__(self):
        return f"It is currently {self.time} and the simulation has been running for {self._timeToString(self.runTime)} hours."
