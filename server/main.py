from fastapi import FastAPI, Request
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from app.graph import app as graph_app, state
from agents.quiz_agent import QuizAgent
from agents.classify_agent import classify_risk

app_fastapi = FastAPI()
quiz = QuizAgent()

@app_fastapi.get("/question")
def get_question():
    if quiz.is_finished():
        return {"message": "quiz_complete"}
    return quiz.next_question()

@app_fastapi.post("/answer")
async def post_answer(req: Request):
    data = await req.json()
    quiz.record_answer(data["answer"])
    if quiz.is_finished():
        result = classify_risk(quiz.get_answers())
        quiz.reset()
        return result
    return quiz.next_question()

@app_fastapi.get("/reset")
def reset():
    quiz.reset()
    return {"message": "reset_success"}