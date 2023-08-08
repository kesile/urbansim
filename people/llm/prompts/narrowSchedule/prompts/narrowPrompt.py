narrowPrompt = """
Hello, your job is to turn this broad schedule into a much more specific, minutely schedule.
The minutely schedule must be by 5 minute increments. Here are some base rules:
- Somebody should not do something twice. They cannot leave to work twice if they have not
already come back from work.

Here's an example:
{
  "8:00 Activity": "Wake up",
  "8:00 Place": "Bedroom",
  "8:05 Activity": "Brush teeth",
  "8:05 Place": "Bathroom",
  "8:10 Activity": "Take a shower",
  "8:10 Place": "Bathroom",
  "8:15 Activity": "Get dressed",
  "8:15 Place": "Bedroom",
  "8:20 Activity": "Have breakfast",
  "8:20 Place": "Kitchen",
  "8:25 Activity": "Pack school bag",
  "8:25 Place": "Living room",
  "8:30 Activity": "Leave for school",
  "8:30 Place": "Outdoors",
  "8:35 Activity": "Walk to bus stop",
  "8:35 Place": "Outdoors",
  "8:40 Activity": "Wait for the bus",
  "8:40 Place": "Bus stop",
  "8:45 Activity": "Board the bus",
  "8:45 Place": "Bus",
  "8:50 Activity": "Arrive at school",
  "8:50 Place": "School",
  "8:55 Activity": "Start classes",
  "8:55 Place": "Classroom"
}
{
  "9:00 Activity": "Wake up",
  "9:00 Place": "Bedroom",
  "9:05 Activity": "Get ready for school",
  "9:05 Place": "Bathroom",
  "9:10 Activity": "Brush teeth",
  "9:10 Place": "Bathroom",
  "9:15 Activity": "Take a shower",
  "9:15 Place": "Bathroom",
  "9:20 Activity": "Get dressed",
  "9:20 Place": "Bedroom",
  "9:25 Activity": "Have breakfast",
  "9:25 Place": "Kitchen",
  "9:30 Activity": "Pack school bag",
  "9:30 Place": "Living room",
  "9:35 Activity": "Leave for school",
  "9:35 Place": "Outdoors",
  "9:40 Activity": "Walk to bus stop",
  "9:40 Place": "Outdoors",
  "9:45 Activity": "Wait for the bus",
  "9:45 Place": "Bus stop",
  "9:50 Activity": "Board the bus",
  "9:50 Place": "Bus",
  "9:55 Activity": "Arrive at school",
  "9:55 Place": "School"
}

This is terrible. They can't do the same thing twice.
If someone leaves for work or school, it will be noted by [LEAVE] (leaving for work) and [ARRIVE] (returning home).
The person may only leave for work at the end of the hour where the activity includes that keyword.

- Even activities such as sleeping should stay as detailed as possible. Describe their dreams, movements,
breathing, etc. The same applies for all other activities, even those of mundane nature such as exercise.

For example: "sleeping", "sleep", etc is BAD
"Curling up in a comfortable position", "Dreaming of a peaceful beach vacation", etc is GOOD

- Follow the provided format in it's entirety. 
- You are required to perform a function call.



Here's the details: 
"""