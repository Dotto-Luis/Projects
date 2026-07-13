import numpy as np
import pandas as pd
import pytest

import preprocessing


@pytest.fixture
def raw_df():
    """Small synthetic dataframe mimicking the NYC yellow taxi schema."""
    pickups = pd.to_datetime(
        [
            "2022-05-02 08:30:00",  # morning, weekday
            "2022-05-02 17:00:00",  # rush hour
            "2022-05-07 23:15:00",  # night, weekend
        ]
    )
    dropoffs = pickups + pd.to_timedelta([15, 30, 10], unit="m")
    return pd.DataFrame(
        {
            "tpep_pickup_datetime": pickups,
            "tpep_dropoff_datetime": dropoffs,
            "trip_distance": [2.5, 8.0, 1.2],
            "passenger_count": [1, 2, 1],
            "fare_amount": [10.0, 35.0, 7.5],
        }
    )


def test_categorize_hour_boundaries():
    assert preprocessing.categorize_hour(6) == "morning"
    assert preprocessing.categorize_hour(12) == "noon"
    assert preprocessing.categorize_hour(13) == "afternoon"
    assert preprocessing.categorize_hour(18) == "evening"
    assert preprocessing.categorize_hour(22) == "night"
    assert preprocessing.categorize_hour(3) == "night"


def test_categorize_rush_hour():
    assert preprocessing.categorize_rush_hour(16) == 1
    assert preprocessing.categorize_rush_hour(20) == 1
    assert preprocessing.categorize_rush_hour(15) == 0
    assert preprocessing.categorize_rush_hour(21) == 0


def test_add_trip_duration_in_minutes(raw_df):
    df = preprocessing.add_trip_duration(raw_df)
    assert list(df["trip_duration"]) == [15.0, 30.0, 10.0]


def test_add_features_with_precomputed_avg_speed(raw_df):
    """Inference path: features derived only from pickup time and distance."""
    avg_speed_dict = {h: 0.2 for h in range(24)}
    df = preprocessing.add_hour_of_day(raw_df)
    df, _ = preprocessing.add_features(df, avg_speed_dict)

    assert list(df["hour_of_day"]) == [8, 17, 23]
    assert list(df["rush_hour"]) == [0, 1, 0]
    assert list(df["day_of_week"]) == [0, 0, 5]
    assert list(df["trip_d2"]) == [2.5**2, 8.0**2, 1.2**2]
    assert (df["avg_speed"] == 0.2).all()


def test_delete_outliers_filters_extremes(raw_df):
    df = preprocessing.add_trip_duration(raw_df)
    # Inject clear outliers
    outlier = df.iloc[[0]].copy()
    outlier["fare_amount"] = 500.0
    outlier["trip_distance"] = 60.0
    df = pd.concat([df, outlier], ignore_index=True)

    cleaned = preprocessing.delete_outliers(df)

    assert len(cleaned) == 3
    assert cleaned["fare_amount"].max() <= 75.0
    assert cleaned["trip_distance"].max() <= 25


def test_split_dataset(raw_df):
    df = preprocessing.add_trip_duration(raw_df)
    X, y = preprocessing.split_dataset(df)

    assert list(y.columns) == ["trip_duration", "fare_amount"]
    assert "trip_duration" not in X.columns
    assert "fare_amount" not in X.columns
    assert len(X) == len(y) == 3
