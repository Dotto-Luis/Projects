import pandas as pd


def load_and_merge_data():
    """
    Load training datasets, parse dates, create basic temporal features,
    merge them into a single dataframe, and return both merged and raw datasets.
    """

    # =========================
    # 1. Load raw datasets
    # =========================
    water_quality = pd.read_csv("../data/water_quality_training_dataset.csv")
    landsat = pd.read_csv("../data/landsat_features_training.csv")
    terraclimate = pd.read_csv("../data/terraclimate_features_training.csv")

    # =========================
    # 2. Parse dates
    # =========================
    for df_tmp in [water_quality, landsat, terraclimate]:
        df_tmp["Sample Date"] = pd.to_datetime(df_tmp["Sample Date"], dayfirst=True)

    # =========================
    # 3. Create temporal features
    # =========================
    water_quality["month"] = water_quality["Sample Date"].dt.month
    water_quality["year"] = water_quality["Sample Date"].dt.year
    water_quality["dayofyear"] = water_quality["Sample Date"].dt.dayofyear

    # =========================
    # 4. Merge datasets
    # =========================
    df = water_quality.merge(
        landsat,
        on=["Latitude", "Longitude", "Sample Date"],
        how="left"
    )

    df = df.merge(
        terraclimate,
        on=["Latitude", "Longitude", "Sample Date"],
        how="left"
    )

    # =========================
    # 5. Fill missing values
    # =========================
    df.fillna(df.median(numeric_only=True), inplace=True)

    # =========================
    # 6. Return merged + raw datasets
    # =========================
    return df, water_quality, landsat, terraclimate