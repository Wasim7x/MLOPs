import os
from pathlib import Path

list_of_files = [
    ".github/workflows",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_training.py",
    "src/components/model_evaluation.py",
    "src/pipelines/__init__.py",
    "src/pipelines/training_pipeline.py",
    "src/pipelines/prediction_pipeline.py",
    "src/utils/__init__.py",
    "tests/unit/__init__.py",
    "src/logger/logging.py",
    "src/exception/exceptions.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requiements.txt",
    "requirements_dev.txt",
    "setup.cfg",
    "setup.py",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiments.ipynb",
    ".gitignore",

]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir, filename = os.path.split(file_path)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Create an empty file if it does not exist or is empty

    
