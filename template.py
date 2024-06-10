import os   # To interact with respective os system
from pathlib import Path   # To convert into suitable path for os system
import logging      # To logging the information for tracking each instruction

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')   # this will help to loggin the information w.r.t time

project_name ="ImageClassification"    # your project name 

# listing down the list directory and file for project structure  template

list_of_files =[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
    ]

# iterating over list of files and split folder and files seperatly and saving it tuple ex: (filedir ,filename)

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir ,filename = os.path.split(filepath)

    ##create directory
    # if the directory/folder is not empty (means must be there atleast one file inside folder) , then create folder  and logging info with created directory 
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info("great job you have created directory :{filedir} for file :{filepath}")

    ##creating file inside folder/directory
    #if the file not present inside folder or file with zero size/empty file then create file inside folder. else logging info as file already exist/created
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
        with open(filepath,'w') as f:
            pass  # craeting empty file only
            logging.info("creating empty file: {filepath}")

    # if file as more than 0 size or file  exist then controller will come to else condition
    else:
        logging.info(f"{filepath} : file is alredy created")

