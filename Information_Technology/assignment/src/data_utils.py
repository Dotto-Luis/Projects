import os
import zipfile

import gdown

from src import config


def download_datasets(output_folder=config.DATASET_ROOT_PATH):
    """
    Download from GDrive all the needed datasets for the project.
    """
    # Create folder if doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder, exist_ok=True)

    # Download dataset from Drive
    output_filename = os.path.join(output_folder, config.ZIP_DATASET_FILENAME)
    if not os.path.exists(output_filename):
        gdown.download(config.DATASET_URL, output_filename, quiet=False)

    # Unzip dataset
    with zipfile.ZipFile(output_filename, "r") as zip_ref:
        zip_ref.extractall(os.path.dirname(output_filename))
