import json
from typing import List, Dict
from pathlib import Path

# Get the project root directory
project_root = Path(__file__).parent.parent
questions_file = project_root / "data" / "questions.json"

with open(questions_file) as f:
    QUESTIONS = json.load(f)

class QuizAgent:
    def __init__(self):
        self.current = 0
        self.answers = []

    def next_question(self) -> Dict:
        if self.current < len(QUESTIONS):
            return QUESTIONS[self.current]
        return None

    def record_answer(self, answer: str):
        self.answers.append(answer)
        self.current += 1

    def is_finished(self) -> bool:
        return self.current >= len(QUESTIONS)

    def get_answers(self) -> List[str]:
        return self.answers

    def reset(self):
        self.current = 0
        self.answers = []