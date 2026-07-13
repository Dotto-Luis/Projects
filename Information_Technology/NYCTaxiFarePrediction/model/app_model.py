import sys
import os
import pandas as pd
from flask import Flask, request, jsonify, Response
import preprocessing
import pickle


model_prefix = os.environ.get("MODEL_PREFIX", "lgbm")
model_name_td = f"{model_prefix}_model_td.model"
model_name_fa = f"{model_prefix}_model_fa.model"

print(model_name_td)
print(model_name_fa)

if model_prefix == "lgbm":
    import lightgbm as lgb

    model_td = lgb.Booster(model_file=model_name_td)
    model_fa = lgb.Booster(model_file=model_name_fa)
else:
    if os.path.exists(model_name_td):
        with open(model_name_td, "rb") as model_td_fd:
            model_td = pickle.load(model_td_fd)
    else:
        print("TD model not found!")

    if os.path.exists(model_name_fa):
        with open(model_name_fa, "rb") as model_fa_fd:
            model_fa = pickle.load(model_fa_fd)
    else:
        print("FA model not found!")

if os.path.exists("encoders.model"):
    with open("encoders.model", "rb") as encoders_file:
        encoders = pickle.load(encoders_file)
else:
    print("Encoders model not found!")

if os.path.exists("avg_speed_dict.model"):
    with open("avg_speed_dict.model", "rb") as avg_speed_dict_fd:
        avg_speed_dict = pickle.load(avg_speed_dict_fd)
else:
    print("Average speed dictionary not found!")


app = Flask(__name__)


def predict_trip(trip_distance, pickup_date, pickup_time):
    """ """
    tpep_pickup_datetime = pickup_date + " " + pickup_time
    data = {
        "trip_distance": [float(trip_distance)],
        "tpep_pickup_datetime": [pd.to_datetime(tpep_pickup_datetime)],
    }
    df = pd.DataFrame(data)
    df, _ = preprocessing.add_features(df, avg_speed_dict)
    df.drop(columns="tpep_pickup_datetime", inplace=True)
    for encoder_model in encoders:
        encoder, col = encoder_model
        array = pd.DataFrame(df[col].values.reshape(1, -1), columns=[col])
        encoded_data = encoder.transform(array)
        encoded_data = encoded_data.toarray()
        encoded_df = pd.DataFrame(
            encoded_data, columns=encoder.get_feature_names_out([col])
        )
        df = pd.concat([df, encoded_df], axis=1, join="inner")
        df.drop(columns=col, inplace=True)
    x = df
    y_fa = round(model_fa.predict(x)[0], 2)
    y_td = int(model_td.predict(x)[0])
    return (y_fa, y_td)


@app.route("/test", methods=["GET"])
def test():
    try:
        pickup_date = "2022/05/16"
        pickup_time = "12:00:00"
        trip_distance = "1.0"
        y_fa, y_td = predict_trip(trip_distance, pickup_date, pickup_time)
        return jsonify(
            {
                "status": ("OK", 200),
                "trip_duration": y_td,
                "fare_amount": y_fa,
            }
        )
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        return Response(
            f"Error {exc_type} in line {exc_tb.tb_lineno}: {e}",
            status=400,
        )


@app.route("/predict", methods=["GET", "POST"])
def predict_endpoint():
    try:
        data = request.get_json()
        trip_distance = data["trip_distance"]
        pickup_date = data["pickup_date"]
        pickup_time = data["pickup_time"]
        y_fa, y_td = predict_trip(trip_distance, pickup_date, pickup_time)
        return jsonify(
            {
                "status": ("OK", 200),
                "trip_duration": y_td,
                "fare_amount": y_fa,
            }
        )
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return Response(
            f"Error {exc_type} in line {exc_tb.tb_lineno}: {e}",
            status=400,
        )


@app.route("/", methods=["GET"])
def index_page():
    try:
        return Response(
            f"This is the index of the model backend. Go to /predict or /test",
            status=200,
        )
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        return Response(
            f"Error {exc_type} in line {exc_tb.tb_lineno}: {e}",
            status=400,
        )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
