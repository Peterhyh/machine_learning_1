import json
from difflib import get_close_matches

# loading knowledge_base.json to this file (program)


def load_knowledge_base(file_path: str):
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data

# saving responses as dictionary to knowledge_base.json


def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# finding the best match from knowledge_base.json


def find_best_match(user_question: str, questions: list[str]):
    matches: list = get_close_matches(
        user_question, questions, n=1, cutoff=0.7)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict):
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]


# programming the chatbot functionality
def chat_bot():
    knowledge_base: dict = load_knowledge_base("knowledge_base.json")

    while True:
        user_input: str = input("You: ")

        if user_input.lower() == "quit":
            break

        # Searching for the best match in knowledge_base.json
        best_match: str | None = find_best_match(user_input.lower(), [q["question"] for q in knowledge_base["questions"]])

        # Bot searching for the answer and responding to user
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot: {answer}")
        else:
            print("Bot: My apologies, I didn't understand. Could you teach me?")
            new_answer: str = input('Type the answer or "no" to skip: ')

            if new_answer.lower() != 'no':
                knowledge_base["questions"].append(
                    {"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print("Thank you! I have learned a new thing!")


if __name__ == '__main__':
    chat_bot()
