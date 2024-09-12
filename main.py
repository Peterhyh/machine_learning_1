import openai

openai.api_key = "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"


def chat_with_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input in ["quit", "exit", "bye"]:
            break
        response = chat_with_ai(user_input)
        print("Chatbot: ", response)
