import openai
API_KEY = "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"

openai.api_key = API_KEY

def narrowText(instructions, person, functions, previous):
    textQuery = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role" : "system", "content" : "Follow all instructions."},
            {"role" : "system", "content" : f"Provided here are the two previous schedules to help with continuity: {previous}"},
            {"role" : "system", "content" : instructions},
            {"role": "user", "content": person}
        ],
        functions = functions,
    )
    if textQuery["choices"][0]["message"]["content"]:
        return narrowText(instructions, person, functions)
    result = textQuery["choices"][0]["message"]["function_call"]["arguments"]
    previous.append(result)
    if len(previous) > 2: previous.pop(0)
    return result
