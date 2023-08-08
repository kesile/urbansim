import openai
API_KEY = "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"

openai.api_key = API_KEY

def textCall(instructions, person, functions):
    textQuery = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {"role" : "system", "content" : "Follow all instructions."},
            {"role" : "system", "content" : instructions},
            {"role": "user", "content": person}
        ],
        functions = functions,
    )
    if textQuery["choices"][0]["message"]["content"]:
        return textCall(instructions, person, functions)
    result = textQuery["choices"][0]["message"]["function_call"]["arguments"]
    return result
