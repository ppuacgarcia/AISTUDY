import openai
openai.api_key = "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"

def ask_gpt(prompt, model, temperature=0.5, max_tokens=50):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    message = response.choices[0].text.strip()
    return message

while True:
    prompt = input("You: ")
    response = ask_gpt(prompt, "davinci")
    print("AI: " + response)
