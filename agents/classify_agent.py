from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(model="llama3.2")

template = PromptTemplate.from_template("""
Based on the user's answers: {answers}, classify their investment risk profile as Conservative, Moderate, or Aggressive.
Give a short explanation (3-4 sentences) justifying the category.
""")

def classify_risk(answers: list) -> dict:
    prompt = template.format(answers=", ".join(answers))
    #print('Prompt: ', prompt)
    response = llm.invoke(prompt)
    return {"classification": response.content.strip()}








