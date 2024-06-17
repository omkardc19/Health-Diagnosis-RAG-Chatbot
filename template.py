import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# List of files to be created
file_list = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt_template.py",
    ".env",
    "setup.py",
    "research/expt_notebook.ipynb",
    "app.py",
    "data_ingestion.py",
    "static/.gitkeep",
    "templates/chat.html"


]

# Create the files
for filepath in file_list:
   filepath = Path(filepath)
   filedir, filename = os.path.split(filepath)

   # Create the directory if it does not exist
   if filedir !="":
      os.makedirs(filedir, exist_ok=True)
      logging.info(f"Creating directory; {filedir} for the file {filename}")

   # Create the file if it does not exist
   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass
         logging.info(f"Creating empty file: {filepath}")

   # Log if the file already exists
   else:
      logging.info(f"{filename} is already created")
      
      
    