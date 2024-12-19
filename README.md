# Formula_Generator
![466026928_940908484153842_2354229892018288957_n](https://github.com/user-attachments/assets/0e8b14ae-55b7-4a81-8034-9cf016cf67d9)
## Project Overview
LaTeX Formula Generator is a web-based application designed to simplify the creation of mathematical and machine learning/deep learning formulas in LaTeX format. The tool provides a user-friendly interface for editing and visualizing formulas while offering the ability to copy the generated LaTeX syntax directly to the clipboard. This ensures seamless integration with LaTeX documents and code, making it a valuable resource for students, researchers, and professionals.
## Technologies Used
- Python
- Ollama – to utilize language model APIs for generating and refining LaTeX formulas.
- Flask – to run the web application and handle backend processes.
- Langchain – to manage interactions and workflows with large language models, enabling advanced LaTeX formula generation.
- HTML/CSS – to design and style the frontend interface for user interaction.
- Javascript - to enable functionality such as copying the generated LaTeX formula to the clipboard.
## Setup
Below are the steps to run the application using Docker.
## Prerequisites
Make sure you have the following installed on your computer:
- Ollama
- Docker
### Step 1: Clone the repository
```bash
git clone https://github.com/72Clooud/LaTeX_Formula_Generator.git
cd LaTeX_Formula_Generator
```
### Step 2: Build the Docker image
```bash
docker build -t latex-formula-generator .
```
### Step 3: Run the container
```bash
docker run -p 5000:5000 latex-formula-generator
```
