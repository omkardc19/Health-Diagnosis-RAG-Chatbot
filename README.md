# Health-Diagnosis-RAG-Chatbot
## Submission for Microsoft Hackathon 2024

## How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/omkardc19/Health-Diagnosis-RAG-Chatbot.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n hchat python=3.9 -y
```

```bash
conda activate hchat
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your credentials as follows:

```ini
GOOGLE_API_KEY = "<YOUR-API-KEY-HERE>" 
PINECONE_API_KEY = "<YOUR-API-KEY-HERE>"
INDEX_NAME = "<YOUR-INDEX-NAME-HERE>"
```
