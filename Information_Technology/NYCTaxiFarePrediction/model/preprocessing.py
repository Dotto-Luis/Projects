import os
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder


hour_zones = [
    "hour_zone_morning",
    "hour_zone_noon",
    "hour_zone_afternoon",
    "hour_zone_evening",
    "hour_zone_night",
]

# order of features is important! -> add_feature()
features = [
    "trip_distance",
    "hour_of_day",
    "rush_hour",
    "day_of_week",
    "trip_d2",
    "avg_speed",
]

# Don't change targets
targets = ["fare_amount", "trip_duration"]


def categorize_hour(hour: int):
    """ """
    if 6 <= hour < 12:
        return "morning"
    elif 12 <= hour < 13:
        return "noon"
    elif 13 <= hour < 18:
        return "afternoon"
    elif 18 <= hour < 22:
        return "evening"
    else:
        return "night"


def categorize_rush_hour(hour: int):
    """ """
    if 16 <= hour <= 20:
        return 1
    else:
        return 0


def add_hour_zone(df: pd.DataFrame):
    """ """
    df["hour_zone"] = df["hour_of_day"].apply(categorize_hour)
    return df


def add_rush_hour(df: pd.DataFrame):
    """ """
    df["rush_hour"] = df["hour_of_day"].apply(categorize_rush_hour)
    return df


def process_outliers(df: pd.DataFrame, action: str = "delete"):
    """ """

    if action == "delete":
        df = delete_outliers(df)
    elif action == "impute":
        df = impute_outliers(df)
    else:
        pass
    return df


def impute_outliers(df: pd.DataFrame):
    """ """

    fare_median = df["fare_amount"].median()
    fare_outliers = df[(df["fare_amount"] < 0) | (df["fare_amount"] > 70)]
    df.loc[fare_outliers.index, "fare_amount"] = fare_median

    trip_duration_median = df["trip_duration"].median()
    trip_duration_outliers = df[(df["trip_duration"] < 0) | (df["trip_duration"] > 75)]
    df.loc[trip_duration_outliers.index, "trip_duration"] = trip_duration_median

    trip_distance_median = df["trip_distance"].median()
    trip_distance_outliers = df[(df["trip_distance"] > 20)]
    df.loc[trip_distance_outliers.index, "trip_distance"] = trip_distance_median

    return df


def delete_outliers(df: pd.DataFrame):
    """
    ** Percentiles for 0.01 **
    trip_distance 0.0
    fare_amount 2.5
    trip_duration 0.38

    ** Percentiles for 0.995 **
    trip_distance 21.78
    fare_amount 71.5
    trip_duration 83.06
    """

    df = df[(df["trip_distance"] >= 0.1) & (df["trip_distance"] <= 25)]

    df = df[(df["fare_amount"] >= 2.5) & (df["fare_amount"] <= 75.0)]

    df = df[(df["trip_duration"] >= 0.25) & (df["trip_duration"] <= 90)]

    df = df[(df["passenger_count"] >= 1) & (df["passenger_count"] <= 6)]

    return df


def fill_na_values(df: pd.DataFrame):
    """ """
    mean_value = int(df["passenger_count"].mean())
    df["passenger_count"].fillna(mean_value, inplace=True)

    median_value = int(df["RatecodeID"].median())
    df["RatecodeID"].fillna(median_value, inplace=True)

    return df


def add_trip_duration(df: pd.DataFrame):
    """ """
    df["trip_duration"] = df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
    df["trip_duration"] = df["trip_duration"].dt.total_seconds() / 60
    return df


def select_features(df: pd.DataFrame, selected_features: list):
    """ """
    return df[selected_features]


def add_day_of_week(df: pd.DataFrame):
    """ """
    df["day_of_week"] = df["tpep_pickup_datetime"].dt.day_of_week
    return df


def build_avg_speed_feature(df: pd.DataFrame):
    """ """
    df = add_avg_speed(df)
    df_avg_speed = df[["hour_of_day", "avg_speed"]]
    avg_speed = df_avg_speed.groupby(["hour_of_day"]).mean()
    avg_speed_dict = avg_speed.to_dict()["avg_speed"]
    return df, avg_speed_dict


def add_avg_speed(df: pd.DataFrame, avg_speed_dict=None):
    """ """
    df["avg_speed"] = df["trip_distance"] / df["trip_duration"]
    return df


def get_avg_speed_hour(df: pd.DataFrame):
    df_avg_speed = df[["hour_of_day", "avg_speed"]]
    avg_speed = df_avg_speed.groupby(["hour_of_day"]).mean()
    avg_speed_dict = avg_speed.to_dict()
    return


def add_hour_of_day(df: pd.DataFrame):
    """ """
    df["hour_of_day"] = df["tpep_pickup_datetime"].dt.hour
    return df


def add_trip_d2(df: pd.DataFrame):
    """ """
    df["trip_d2"] = df["trip_distance"] ** 2
    return df


def add_vendor_encoding(df: pd.DataFrame):
    encoder = OneHotEncoder()
    encoded_data = encoder.fit_transform(df[["VendorID"]])
    encoded_df = pd.DataFrame(
        encoded_data.toarray(), columns=encoder.get_feature_names_out(["VendorID"])
    )
    final_df = pd.concat([df, encoded_df], axis=1, join="inner")
    final_df.drop(columns="VendorID", inplace=True)
    return final_df, (encoder, "VendorID")


def add_hourzone_encoding(df: pd.DataFrame):
    encoder = OneHotEncoder()
    encoded_data = encoder.fit_transform(df[["hour_zone"]])
    encoded_df = pd.DataFrame(
        encoded_data.toarray(), columns=encoder.get_feature_names_out(["hour_zone"])
    )
    final_df = pd.concat([df, encoded_df], axis=1, join="inner")
    final_df.drop(columns="hour_zone", inplace=True)
    return final_df, (encoder, "hour_zone")


def add_targets(df: pd.DataFrame):
    """ """
    df = add_trip_duration(df)
    return df


def add_features(df: pd.DataFrame, avg_speed_dict=None):
    """ """
    # order of features is important!
    df = add_hour_of_day(df)
    df = add_rush_hour(df)
    df = add_day_of_week(df)
    df = add_trip_d2(df)

    if avg_speed_dict is None:
        print("Building average speed dictionary")
        df, avg_speed_dict = build_avg_speed_feature(df)
    else:
        print("Using pre-processed average speed dictionary")
        df['avg_speed'] = df['hour_of_day'].map(avg_speed_dict)
    return df, avg_speed_dict


def create_one_hot_encodings(df: pd.DataFrame, features: str):
    """ """
    encoders = []

    if "vendor_id" in features:
        df, encoder = add_vendor_encoding(df)
        encoders.append(encoder)
    if "hour_zone" in features:
        df, encoder = add_hourzone_encoding(df)
        encoders.append(encoder)

    return df, encoders


def split_dataset(df: pd.DataFrame):
    y = df[["trip_duration", "fare_amount"]]
    X = df.drop(columns=["trip_duration", "fare_amount"], inplace=False)
    return X, y


def process_inference():
    pass
