import os
import re

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from flask import Flask, request, render_template, url_for
from io import BytesIO
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, template_folder='template', static_folder='static')


template = """
You are a LaTeX formula generator. Your ONLY task is to output LaTeX formulas. Do not include any explanation, any extra words, or any context. Your responses MUST ONLY consist of LaTeX code enclosed in double dollar signs `$$`.

Here is the user's question: {question}

Output ONLY the formula enclosed in `$$`, without any extra text:
"""



model = OllamaLLM(model="Mistral", temperature=0)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def extract_latex_only(response):
    match = re.search(r'\$\$(.*?)\$\$', response, re.DOTALL)
    if match:
        return f"$${match.group(1)}$$"
    else:
        return "Error: No valid LaTeX found"

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        question = request.form.get("question")
        result = chain.invoke({"question": question, "reset_context": True})
        result = extract_latex_only(result)
        return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'), debug=True)