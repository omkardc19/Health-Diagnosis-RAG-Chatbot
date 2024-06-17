from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings



load_dotenv()

# Load CSV files from the specified directory
def load_csv(data_directory):
    # Use DirectoryLoader to load all CSV files from the specified directory
    loader = DirectoryLoader(
        data_directory,
        glob="*.csv",        # Pattern to match CSV files
        loader_cls=CSVLoader # Use CSVLoader to load the files
    )
    
    # Load the documents
    documents = loader.load()

    return documents


# Split the extracted data into text chunks
def text_split(extracted_data):
    # Initialize the text splitter with desired chunk size and overlap
      text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
    
    # Split the extracted data into text chunks
      all_splits = text_splitter.split_documents(extracted_data)

      return all_splits


# Load the Google Generative AI Embeddings model
def download_google_embeddings():
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    # Initialize the Google Generative AI Embeddings model
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
                                        
    return embeddings