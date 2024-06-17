from flask import Flask, request, jsonify, render_template
from src.helper import download_google_embeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_pinecone import PineconeVectorStore
import os
# from langchain import PromptTemplate
from langchain_core.prompts import PromptTemplate
import google.generativeai as genai
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt_template import *

# Load the environment variables
load_dotenv()

# Get the Pinecone API key and index name
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("INDEX_NAME")

# Downloading the Google Generative AI Embeddings
embeddings = download_google_embeddings()

# Initializing the Pinecone with existing index
docsearch = PineconeVectorStore.from_existing_index(INDEX_NAME, embeddings)

# Initialize the Flask app
app = Flask(__name__)

# import and define the prompt template
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# Define the chain type and kwargs
chain_type_kwargs = {"prompt": PROMPT}

# Initialize the language model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    # google_api_key=app.config['GOOGLE_API_KEY'],
    temperature=0.8,
    max_output_tokens=512
)

# Create QA chain
qa = RetrievalQA.from_chain_type(
    llm=model,
    chain_type="stuff",
    retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 5}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

# Define the route for the chatbot
@app.route('/')
def index():
    return render_template('index.html')

# # Define the route for the chatbot
# @app.route("/get", methods=["GET", "POST"])
# def chat():
#     msg = request.form["msg"]
#     input = msg
#     print(input)
#     result=qa({"query": input})
#     print("Response : ", result["result"])
#     return str(result["result"])


# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)