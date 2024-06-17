# Health-Diagnosis-RAG-Chatbot
## Submission for Microsoft Hackathon 2024

# How to run?
### STEPS:

### STEP 01- Clone the repository

```bash
git clone https://github.com/omkardc19/Health-Diagnosis-RAG-Chatbot.git
```

### STEP 02- Create a conda environment after opening the repository

```bash
conda create -n hchat python=3.8 -y
```

```bash
conda activate hchat
```

### STEP 03- install the requirements
```bash
pip install -r requirements.txt
```


### STEP 03- Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
GOOGLE_API_KEY = "<YOUR-API-KEY-HERE>" 
PINECONE_API_KEY = "<YOUR-API-KEY-HERE>"
INDEX_NAME = "<YOUR-INDEX-NAME-HERE>"
```
