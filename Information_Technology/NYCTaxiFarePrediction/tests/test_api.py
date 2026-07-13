import json
from unittest.mock import MagicMock, patch

import pytest

from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_index_alive(client):
    response = client.get("/")
    assert response.status_code == 200


@patch("views.requests.post")
def test_predict_forwards_to_model_service(post_mock, client):
    """The gateway forwards the payload to the model service and returns
    fare and duration."""
    model_response = MagicMock()
    model_response.status_code = 200
    model_response.json.return_value = {"fare_amount": 18.5, "trip_duration": 22.3}
    post_mock.return_value = model_response

    payload = {
        "trip_distance": "5.2",
        "pickup_date": "2022-05-02",
        "pickup_time": "17:30",
    }
    response = client.post(
        "/predict", data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 200
    data = response.get_json()
    assert data == {"fare": 18.5, "duration": 22.3}

    sent = post_mock.call_args.kwargs["json"]
    assert sent["trip_distance"] == 5.2
    assert sent["pickup_date"] == "2022-05-02"


@patch("views.requests.post")
def test_predict_handles_model_service_error(post_mock, client):
    """If the model service fails, the gateway degrades gracefully."""
    model_response = MagicMock()
    model_response.status_code = 500
    model_response.text = "boom"
    post_mock.return_value = model_response

    payload = {
        "trip_distance": "5.2",
        "pickup_date": "2022-05-02",
        "pickup_time": "17:30",
    }
    response = client.post(
        "/predict", data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 200
    data = response.get_json()
    assert data == {"fare": -1, "duration": -1}
