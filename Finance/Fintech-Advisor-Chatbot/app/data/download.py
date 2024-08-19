import boto3
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

aws_access_key_id = 'YOUR_ACCESS_KEY'
aws_secret_access_key = 'YOUR_SECRET_KEY'
bucket_name = 'anyoneai-datasets'
file_key = 'nasdaq_annual_reports/your_file.csv'

project_dir = os.path.dirname(os.path.abspath(__file__))
raw_data_dir = os.path.join(project_dir, '..', 'data', 'raw')
os.makedirs(raw_data_dir, exist_ok=True)
local_file_path = os.path.join(raw_data_dir, 'local_file.csv')

try:
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    s3.download_file(bucket_name, file_key, local_file_path)
    print(f"Archivo descargado en {local_file_path}")
except NoCredentialsError:
    print("No se encontraron credenciales de AWS.")
except PartialCredentialsError:
    print("Las credenciales de AWS están incompletas.")
except ClientError as e:
    print(f"Error al descargar el archivo: {e}")
