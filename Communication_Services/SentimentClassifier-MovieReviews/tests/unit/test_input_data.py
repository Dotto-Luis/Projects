from src import data_utils


def test_splitted_data():
    train, test = data_utils.get_datasets()
    X_train, y_train, X_test, y_test = data_utils.split_data(train, test)

    assert len(X_train) == 25000, "Dimensions do not match!"
    assert len(y_train) == 25000, "Dimensions do not match!"
    assert len(X_test) == 25000, "Dimensions do not match!"
    assert len(y_test) == 25000, "Dimensions do not match!"
