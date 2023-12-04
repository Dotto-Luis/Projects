import os
from pathlib import Path

DATASET_ROOT_PATH = str(Path(__file__).parent.parent / "dataset")
os.makedirs(DATASET_ROOT_PATH, exist_ok=True)

DATASET_TRAIN = str(Path(DATASET_ROOT_PATH) / "movies_review_train_aai.csv")
DATASET_TRAIN_URL = "https://drive.google.com/uc?id=1nSeixkiFj1zmK5-Eo6gA3Ak4doJguzNm"
DATASET_TEST = str(Path(DATASET_ROOT_PATH) / "movies_review_test_aai.csv")
DATASET_TEST_URL = "https://drive.google.com/uc?id=18Fx4HPofqXsIzQZIYoaroa4o1VSMx9-H"
