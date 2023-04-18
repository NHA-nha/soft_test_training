import openai

OPENAI_API_KEY = "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"
while True:
    content = input("User('exit' to quit): ")
    if content == "exit":
        print('ChatGPT: See you next time!')
        break
    messages = []
    messages.append({"role": "user", "content": content})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=messages,
        temperature=0.9,
        max_tokens=1000,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"],
        api_key=OPENAI_API_KEY,
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')
    # messages.append({"role": "assistant", "content": chat_response})
