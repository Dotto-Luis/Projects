import numpy as np
import pytest
from tensorflow.keras.layers import Conv2D, Dense
from tensorflow.keras.models import Sequential

from src.models import create_lenet_model, create_mlp_model, create_resnet50_model


@pytest.fixture
def input_shape():
    return (32, 32, 3)


@pytest.fixture
def num_classes():
    return 10


def test_create_mlp_model_returns_sequential_model(input_shape, num_classes):
    model = create_mlp_model(input_shape, num_classes)
    assert isinstance(model, Sequential)


def test_create_mlp_model_correct_input_shape(input_shape, num_classes):
    model = create_mlp_model(input_shape, num_classes)
    assert model.input_shape == (None, *input_shape)


def test_create_mlp_model_correct_output_shape(input_shape, num_classes):
    model = create_mlp_model(input_shape, num_classes)
    assert model.output_shape == (None, num_classes)


def test_create_mlp_model_layer_number(input_shape, num_classes):
    model = create_mlp_model(input_shape, num_classes)
    assert len(model.layers) == 6, f"Expected 6 layers, got {len(model.layers)}"


def test_create_mlp_model_activation(input_shape, num_classes):
    model = create_mlp_model(input_shape, num_classes)
    msg = f"Expected layer {model.layers[2]} activation to be relu"
    assert model.layers[2].activation.__name__ == "relu", msg

    msg = (f"Expected layer {model.layers[3]} activation to be relu",)
    assert model.layers[3].activation.__name__ == "relu", msg

    msg = f"Expected layer {model.layers[4]} activation to be relu"
    assert model.layers[4].activation.__name__ == "relu", msg

    msg = f"Expected layer {model.layers[5]} activation to be softmax"
    assert model.layers[5].activation.__name__ == "softmax", msg


def test_create_mlp_model_num_neurons(input_shape, num_classes):
    model = create_mlp_model(input_shape, num_classes)
    expected_neurons = [None, None, 512, 1024, 512, num_classes]
    for i, layer in enumerate(model.layers):
        if isinstance(layer, Dense):
            msg = (
                f"Layer {i+1} has {layer.units} neurons, "
                f"but expected {expected_neurons[i]}"
            )
            assert layer.units == expected_neurons[i], msg


def test_create_lenet_model_returns_model_object(input_shape, num_classes):
    model = create_lenet_model(input_shape, num_classes)

    assert isinstance(model, Sequential)


def test_create_lenet_model_has_correct_number_of_layers(input_shape, num_classes):
    model = create_lenet_model(input_shape, num_classes)

    assert len(model.layers) == 9


def test_create_lenet_model_has_correct_layer_activation_functions(
    input_shape, num_classes
):
    model = create_lenet_model(input_shape, num_classes)

    expected_activations = [
        None,
        "tanh",
        None,
        "tanh",
        None,
        None,
        "tanh",
        "tanh",
        "softmax",
    ]
    layer_activations = [
        layer.activation.__name__
        if hasattr(layer, "activation") and layer.activation is not None
        else None
        for layer in model.layers
    ]

    assert layer_activations == expected_activations


def test_create_lenet_model_has_correct_number_of_neurons(input_shape, num_classes):
    model = create_lenet_model(input_shape, num_classes)

    msg = f"Expected layer {model.layers[1]} filters to be 6"
    assert model.layers[1].filters == 6, msg
    msg = f"Expected layer {model.layers[1]} kernel_size to be (3, 3)"
    assert model.layers[1].kernel_size == (3, 3), msg

    msg = f"Expected layer {model.layers[3]} filters to be 16"
    assert model.layers[3].filters == 16, msg
    msg = f"Expected layer {model.layers[3]} kernel_size to be (3, 3)"
    assert model.layers[3].kernel_size == (3, 3), msg

    msg = f"Expected layer {model.layers[6]} units to be 120"
    assert model.layers[6].units == 120, msg

    msg = f"Expected layer {model.layers[7]} units to be 84"
    assert model.layers[7].units == 84, msg

    msg = f"Expected layer {model.layers[8]} units to be {num_classes}"
    assert model.layers[8].units == num_classes, msg


def test_create_lenet_model_output_shape_is_correct(input_shape, num_classes):
    model = create_lenet_model(input_shape, num_classes)

    output_shape = model.predict(np.zeros((1, *input_shape))).shape[1]

    assert output_shape == num_classes


def test_create_resnet50_model_return_type(input_shape, num_classes):
    model = create_resnet50_model(input_shape, num_classes)
    assert isinstance(model, Sequential)


def test_create_resnet50_model_layer_count(input_shape, num_classes):
    model = create_resnet50_model(input_shape, num_classes)
    assert len(model.layers) == 4


def test_create_resnet50_model_last_layer_activation(input_shape, num_classes):
    model = create_resnet50_model(input_shape, num_classes)
    last_layer = model.layers[-1]
    assert last_layer.activation.__name__ == "softmax"
