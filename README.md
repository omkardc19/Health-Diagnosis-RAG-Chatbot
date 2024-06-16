# Health-Diagnosis-RAG-Chatbot
## Submission for Microsoft Hackathon 2024

# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/omkardc19/Health-Diagnosis-RAG-Chatbot.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n hchat python=3.8 -y
```

```bash
conda activate hchat
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```