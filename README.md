# Health-Diagnosis-RAG-Chatbot
## Submission for Microsoft's AI Hackathon 2024
##  [Submission video](https://www.youtube.com/watch?v=example)

## How to run?
### STEPS:

### STEP 01- Clone the repository

```bash
git clone https://github.com/omkardc19/Health-Diagnosis-RAG-Chatbot.git
```

### STEP 02- Create a conda environment after opening the repository

```bash
# run the following command
conda create -n hchat python=3.9 -y
```

```bash
# run the following command
conda activate hchat
```

### STEP 03- install the requirements
```bash
# run the following command
pip install -r requirements.txt
```


### STEP 04- Create a `.env` file in the root directory and add your credentials as follows:
For MS hackathon submission keys are added in a shared g-drive link in "API_Keys.txt"

```ini
GOOGLE_API_KEY = "<YOUR-API-KEY-HERE>" 
PINECONE_API_KEY = "<YOUR-API-KEY-HERE>"
INDEX_NAME = "<YOUR-INDEX-NAME-HERE>"
```
### STEP 05- Store vector embeddings to vector database (if data not ingested beforehand to vector database- Pinecone here)
```bash
# run the following command
python data_ingestion.py
```
### STEP 06- Run the app
```bash
# Finally run the following command
python app.py
```
Finally,
```bash
open up localhost:
```

## Techstack :

- Python
- LangChain
- Flask
- Google Gemini LLM
- Pinecone(free tier)
