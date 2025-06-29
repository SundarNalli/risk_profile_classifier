import sys
import os
from pathlib import Path
from typing import TypedDict, Annotated

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from langgraph.graph import StateGraph, START, END
from agents.quiz_agent import QuizAgent
from agents.classify_agent import classify_risk

class State(TypedDict):
    quiz: QuizAgent
    result: dict

state = {"quiz": QuizAgent()}

def ask_question(state: dict) -> dict:
    question = state["quiz"].next_question()
    if question:
        print("Q:", question["question"])
        for i, opt in enumerate(question["options"]):
            print(f"{i + 1}. {opt}")
        choice = input("Your choice: ")
        answer = question["options"][int(choice)-1]
        state["quiz"].record_answer(answer)
    return state

def check_done(state):
    return "classify" if state["quiz"].is_finished() else "ask"

def classify(state):
    result = classify_risk(state["quiz"].get_answers())
    state["result"] = result
    return state

builder = StateGraph(State)
builder.add_node("ask", ask_question)
builder.add_node("classify", classify)
builder.set_entry_point("ask")
builder.add_conditional_edges("ask", check_done, {
    "ask": "ask",
    "classify": "classify"
})
builder.add_edge("classify", END)

app = builder.compile()
