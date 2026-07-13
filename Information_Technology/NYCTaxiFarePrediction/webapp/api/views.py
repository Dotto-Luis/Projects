import requests
from flask import (
    Blueprint,
    jsonify,
    request,
)

router = Blueprint("app_router", __name__, template_folder="templates")

MODEL_URL = "http://modelsvc:5000/predict"


@router.route("/")
def hello_world():
    return "<h1>Hello World! This is the API of NYC Taxi Prediction. [200] Status</h1>"


@router.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get input data from the form
        json_data = request.json
        trip_distance = float(json_data["trip_distance"])
        pickup_date = json_data["pickup_date"]
        pickup_time = json_data["pickup_time"]
        data = {
            "trip_distance": trip_distance,
            "pickup_date": pickup_date,
            "pickup_time": pickup_time,
        }
        response = requests.post(MODEL_URL, json=data)
        # Checking the response
        if response.status_code == 200:  # Check for the appropriate status code
            print("POST request successful!")
            print("Response:", response.json())  # Print the response content
            predictions = response.json()
            fare = predictions["fare_amount"]
            duration = predictions["trip_duration"]
        else:
            print("POST request failed with status code:", response.status_code)
            print(
                "Error message:", response.text
            )  # Print the error message if request failed
            fare, duration = -1, -1
        return jsonify({"fare": fare, "duration": duration})
