def promptCompiler(people):
    initWrapper = f"""
    keyDirections = "Hello, your job is to simulate an interaction between these {len(people)} people. 
    You will be provided their details and personality, alongside a topic for discussion."

    rules = [
    "Interactions must be as realistic as possible, attempting to accurately simulate people.",
    "If necessary, strong/vulgar language may be used. It should not always be used.",
    "You must pay attention to the environment in order to determine the appropriate level
    of formality, etc.",
    "Do not include anything other than the dialogue: no reflections, context, pre nor proceeding message.",
    "Don't have them try and fix people. If someone is mean, they're mean and should act like it. We're doing
    real world simulation.",
    "Don't have the people mention their personality. Only act like it.",
    "Always use their names during simulations.",
    "Make it sound real, like a human would.",
    "Don't sound corny."
    ]

    people = [
    """
    peopleProfile = ""
    for person in people:
        personString = ""
        personString = personString + f"""
        {person.name} is a {person.age} year old {person.race} {person.gender}
        They work as a {person.job}. {person.personality}\n
        """
        peopleProfile = peopleProfile + personString
    endWrapper = """
    ]

    message = "Ensure you stay accurate to the rules, directions, and people."
    """

    overall = initWrapper + peopleProfile + endWrapper
    return overall