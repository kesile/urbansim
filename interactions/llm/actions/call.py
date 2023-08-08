import openai
API_KEY = "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"

openai.api_key = API_KEY

def conversation(instructions, topic):
    textQuery = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role" : "system", "content" : instructions},
            {"role" : "system", "content" : f"Topic: {topic}"},
        ],
    )
    return textQuery["choices"][0]["message"]["content"]
