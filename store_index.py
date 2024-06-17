from src.helper import load_csv, text_split, download_google_embeddings
from langchain_community.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("INDEX_NAME")

print(PINECONE_API_KEY)
print(INDEX_NAME)