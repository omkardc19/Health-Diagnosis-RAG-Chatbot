from src.helper import load_csv, text_split, download_google_embeddings
from langchain_pinecone import PineconeVectorStore
# from langchain_community.vectorstores import Pinecone
# import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

# Get the Pinecone API key and index name
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY") 
INDEX_NAME = os.getenv("INDEX_NAME")          

extracted_data = load_csv("data/")    # Load the data
text_splits = text_split(extracted_data)  # Split the data into text chunks

# Downloading the Google Generative AI Embeddings
embeddings= download_google_embeddings()


#Initializing the Pinecone
vectorstore = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)

#Creating Embeddings for Each of The Text Chunks & storing
vectorstore.add_documents(text_splits)