import openai

openai.api_key = ""


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
