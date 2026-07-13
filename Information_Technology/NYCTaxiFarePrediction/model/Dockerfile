# Use the official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the Flask app code into the container
COPY * .

# Expose the port the app runs on
EXPOSE 5000

# Model selection
ARG MODEL_PREFIX=lgbm

# Command to run the Flask application
CMD ["python", "app_model.py"]