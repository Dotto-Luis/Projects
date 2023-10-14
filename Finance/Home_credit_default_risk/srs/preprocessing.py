from typing import Tuple

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, OrdinalEncoder


def preprocess_data(
    train_df: pd.DataFrame, val_df: pd.DataFrame, test_df: pd.DataFrame
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Pre processes data for modeling. Receives train, val and test dataframes
    and returns numpy ndarrays of cleaned up dataframes with feature engineering
    already performed.

    Arguments:
        train_df : pd.DataFrame
        val_df : pd.DataFrame
        test_df : pd.DataFrame

    Returns:
        train : np.ndarrary
        val : np.ndarrary
        test : np.ndarrary
    """
    # Print shape of input data
    print("Input train data shape: ", train_df.shape)
    print("Input val data shape: ", val_df.shape)
    print("Input test data shape: ", test_df.shape, "\n")

    # Make a copy of the dataframes
    working_train_df = train_df.copy()
    working_val_df = val_df.copy()
    working_test_df = test_df.copy()

    # 1. Correct outliers/anomalous values in numerical
    # columns (`DAYS_EMPLOYED` column).
    working_train_df["DAYS_EMPLOYED"].replace({365243: np.nan}, inplace=True)
    working_val_df["DAYS_EMPLOYED"].replace({365243: np.nan}, inplace=True)
    working_test_df["DAYS_EMPLOYED"].replace({365243: np.nan}, inplace=True)

    # 2. TODO Encode string categorical features (dytpe `object`):
    #     - If the feature has 2 categories encode using binary encoding,
    #       please use `sklearn.preprocessing.OrdinalEncoder()`. Only 4 columns
    #       from the dataset should have 2 categories.
    #     - If it has more than 2 categories, use one-hot encoding, please use
    #       `sklearn.preprocessing.OneHotEncoder()`. 12 columns
    #       from the dataset should have more than 2 categories.
    # Take into account that:
    #   - You must apply this to the 3 DataFrames (working_train_df, working_val_df,
    #     working_test_df).
    #   - In order to prevent overfitting and avoid Data Leakage you must use only
    #     working_train_df DataFrame to fit the OrdinalEncoder and
    #     OneHotEncoder classes, then use the fitted models to transform all the
    #     datasets.

    # Identify categorical columns to be encoded
    def get_categorical_columns(df, list1, list2):
        col = df.select_dtypes(include=["object"]).nunique() == 2
        for name, value in col.items():
            if value == True:
                list1.append(name)
            else:
                list2.append(name)
        return list

    ordinal_col = []
    onehot_col = []

    get_categorical_columns(working_train_df, ordinal_col, onehot_col)

    # Apply Ordinal Encoder to columns with 2 categories
    ordinal_encoder = OrdinalEncoder()
    ordinal_encoder.fit(working_train_df[ordinal_col])

    datasets = [working_train_df, working_val_df, working_test_df]

    for df in datasets:
        df[ordinal_col] = ordinal_encoder.transform(df[ordinal_col])

    # Apply OneHot Encoder to columns with more than 2 categories
    onehot_encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
    onehot_encoder.fit(working_train_df[onehot_col])

    # Helper function to apply OneHot Encoder
    def oe_encoding(df, col=onehot_col):
        working_onehot = onehot_encoder.transform(df[col])
        df_onehot = pd.DataFrame(
            working_onehot,
            columns=onehot_encoder.get_feature_names_out(),
            index=df.index,
        )
        df_onehot = pd.concat([df_onehot, df], axis=1).drop(col, axis=1)
        return df_onehot

    df_test = oe_encoding(working_test_df)
    df_train = oe_encoding(working_train_df)
    df_val = oe_encoding(working_val_df)

    # 3. TODO Impute values for all columns with missing data or, just all the columns.
    # Use median as imputing value. Please use sklearn.impute.SimpleImputer().
    # Again, take into account that:
    #   - You must apply this to the 3 DataFrames (working_train_df, working_val_df,
    #     working_test_df).
    #   - In order to prevent overfitting and avoid Data Leakage you must use only
    #     working_train_df DataFrame to fit the SimpleImputer and then use the fitted
    #     model to transform all the datasets.'
    # Create a copy of the DataFrames to avoid modifications to the originals

    # Use SimpleImputer to handle missing values and prevent data leakage
    imputer = SimpleImputer(strategy="median", missing_values=np.nan)
    imputer.fit(df_train)

    # Helper function to apply imputation
    def impute_data(imputer, *dataframes):
        imputed_dataframes = [imputer.transform(df) for df in dataframes]
        return imputed_dataframes

    working_train_array, working_test_array, working_val_array = impute_data(
        imputer, df_train, df_test, df_val
    )

    # 4. TODO Feature scaling with Min-Max scaler. Apply this to all the columns.
    # Please use sklearn.preprocessing.MinMaxScaler().
    # Again, take into account that:
    #   - You must apply this to the 3 DataFrames (working_train_df, working_val_df,
    #     working_test_df).
    #   - In order to prevent overfitting and avoid Data Leakage you must use only
    #     working_train_df DataFrame to fit the MinMaxScaler and then use the fitted
    #     model to transform all the datasets.
    # Create the Min-Max scaler

    min_max = MinMaxScaler()
    min_max.fit(working_train_array)

    # Helper function to apply scaling
    def scale_data(scaler, *dataarrays):
        scaled_data = [scaler.transform(data) for data in dataarrays]
        return scaled_data

    working_train_array, working_test_array, working_val_array = scale_data(
        min_max, working_train_array, working_test_array, working_val_array
    )

    return working_train_array, working_val_array, working_test_array
