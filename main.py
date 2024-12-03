from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from sympy.printing.preview import preview

template = """
You are an AI specialized in generating mathematical and machine learning formulas in LaTeX. For the given question, provide only the LaTeX formula as output. Do not include any additional text, explanations, or comments. Return the result formatted between $$ symbols.

Here is the question: {question}

"""

model = OllamaLLM(model="Mistral")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    question = input("try: ")
    if question.lower() == "exit":
        break 
    result = chain.invoke({"question": question})
    print(result)
