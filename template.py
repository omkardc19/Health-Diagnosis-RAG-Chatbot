import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


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


for filepath in file_list:
   filepath = Path(filepath)
   filedir, filename = os.path.split(filepath)

   if filedir !="":
      os.makedirs(filedir, exist_ok=True)
      logging.info(f"Creating directory; {filedir} for the file {filename}")

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass
         logging.info(f"Creating empty file: {filepath}")

   else:
      logging.info(f"{filename} is already created")
      
      
    