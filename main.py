import json


# loading knowledge_base.json to this file (program)
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data

# saving responses as dictionary to knowledge_base.json


def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# finding the best match from knowledge_base.json


def find_best_match(user_question: str, questions: list[str]) -> str:
