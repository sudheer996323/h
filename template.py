import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name='mlProject'

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


]
def create_files(file_paths):
    for file_path in file_paths:
        file_path=Path(file_path)
        filedir=file_path.parent
        if filedir:
            os.makedirs(filedir,exist_ok=True)
            logging.info(f'file directory name {filedir} created')
        if not file_path.exists():
            file_path.touch()
            logging.info(f'file name {file_path} created')
        else:
            logging.info(f'file already {file_path} exists')
create_files(list_of_files)