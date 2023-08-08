weekdayScheduleInstructions = """
Hello, you're going to make a schedule for this person. 
It should be a weekday schedule, and should include the
following rules.
- If the perosn has a job, they must go to work.
- If the person has hobbies, they must participate in at least
one for an hour.
- The person must always get at least 5 hours of sleep.
- If somebody is under 18, they must go to school.

The schedule must be detailed, and should describe their actions.

If someone leaves for work or school, the activity must end with [LEAVE]. Same for [RETURN] when they get back home.
 
You are required to perform a function call.
"""