import os

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from sympy.printing.preview import preview

from flask import Flask, request, render_template
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, template_folder='template')


template = """
You are an AI specialized in generating mathematical and machine learning formulas in LaTeX. For the given question, provide only the LaTeX formula as output. Do not include any additional text, explanations, or comments. Return the result formatted between $$ symbols.

Here is the question: {question}
"""

model = OllamaLLM(model="Mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        question = request.form.get("question")
        result = chain.invoke({"question": question})
        return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'), debug=True)