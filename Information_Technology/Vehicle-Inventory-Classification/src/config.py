import os
from pathlib import Path

DATASET_ROOT_PATH = str(Path(__file__).parent.parent / "dataset")
os.makedirs(DATASET_ROOT_PATH, exist_ok=True)

DATASET_URL = (
    "https://drive.google.com/uc?id=1ueaI8NJLS73Eq8Kx9ctdy5hK3vD53_Jb&confirm=t"
)
ZIP_DATASET_FILENAME = "cars_25_dataset.zip"
DATASET_FILENAME = "eu-car-dataset_subset"
