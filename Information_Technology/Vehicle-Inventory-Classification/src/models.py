from typing import Tuple

from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import (
    AveragePooling2D,
    Conv2D,
    Dense,
    Dropout,
    Flatten,
    Input,
    Rescaling,
)
from tensorflow.keras.models import Sequential


def create_mlp_model(input_shape: Tuple[int, int, int], num_classes: int) -> Sequential:
    """Creates a Multi-layer perceptron model using Keras.

    Args:
        input_shape (Tuple[int, int, int]): The shape of the input data.
        num_classes (int): The number of output classes.

    Returns:
        A Sequential model object with the specified MLP architecture.
    """
    # Define the model
    model = Sequential()

    # Add the input layer
    model.add(Input(shape=input_shape))

    # Layer 0: Rescaling operation to map image pixels from [0, 255] to [0, 1] range
    model.add(Rescaling(1.0 / 255, input_shape=input_shape))

    # Layer 1: Flatten layer to convert the 3D input image to a 1D array
    model.add(Flatten())

    # Adding hidden layers to the model
    # Layer 2: Fully connected layer with 512 neurons,
    # followed by a relu activation function
    # TODO
    model.add(...)

    # Layer 3: Fully connected layer with 1024 neurons,
    # followed by a relu activation function
    # TODO
    model.add(...)

    # Layer 4: Fully connected layer with 512 neurons,
    # followed by a relu activation function
    # TODO
    model.add(...)

    # Layer 5: Classification layer with num_classes output units,
    # followed by a softmax activation function
    # TODO
    model.add(...)

    # Print a summary of the model architecture
    print(model.summary())

    return model


def create_lenet_model(
    input_shape: Tuple[int, int, int], num_classes: int
) -> Sequential:
    """
    Creates a LeNet convolutional neural network model. For reference see original
    publication: http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf.

    Args:
        input_shape (Tuple[int, int, int]): The shape of the input data.
        num_classes (int): The number of output classes.

    Returns:
        A Sequential model object representing the LeNet architecture.
    """
    # Define the model
    model = Sequential()

    # Add the input layer
    model.add(Input(shape=input_shape))

    # Layer 0: Rescaling operation to map image pixels from [0, 255] to [0, 1] range
    model.add(Rescaling(1.0 / 255, input_shape=input_shape))

    # Layer 1: Convolutional layer with 6 filters, each 3x3 in size,
    # followed by a tanh activation function
    # TODO
    model.add(...)

    # Layer 2: Average pooling layer with 2x2 pool size
    # TODO
    model.add(...)

    # Layer 3: Convolutional layer with 16 filters, each 3x3 in size,
    # followed by a tanh activation function
    # TODO
    model.add(...)

    # Layer 4: Average pooling layer with 2x2 pool size
    # TODO
    model.add(...)

    # Layer 5: Flatten layer to convert the output of the previous layer to a 1D array
    # TODO
    model.add(...)

    # Layer 6: Fully connected layer with 120 neurons,
    # followed by a tanh activation function
    # TODO
    model.add(...)

    # Layer 7: Fully connected layer with 84 neurons,
    # followed by a tanh activation function
    # TODO
    model.add(...)

    # Layer 8: Classification layer with num_classes output units,
    # followed by a softmax activation function
    # TODO
    model.add(...)

    # Print a summary of the model architecture
    print(model.summary())

    return model


def create_resnet50_model(
    input_shape: Tuple[int, int, int], num_classes: int
) -> Sequential:
    """
    Function to create a convolutional neural network model based on ResNet50
    architecture with transfer learning.

    Args:
        input_shape (Tuple[int, int, int]): The shape of the input data.
        num_classes (int): The number of output classes.

    Returns:
        A Sequential model object.
    """
    # Create ResNet50 model for transfer learning (fine-tuning).
    # Use `tensorflow.keras.applications.ResNet50()` and make sure to:
    #   1. Use "imagenet" weights
    #   2. Don't include the classification layer (include_top=False)
    #   3. Define model input_shape equals to this function input_shape
    # TODO
    resnet = ...

    # You shouldn't change the code below
    # Freeze all layers in the ResNet50 model
    for layer in resnet.layers:
        layer.trainable = False

    # Define the model
    model = Sequential()

    # Add the resnet model to the Sequential model.
    # We don't need to add Input or Rescaling layers to the model because
    # ResNet50 model already have hose layers inside.
    model.add(resnet)

    # Add a flatten layer to convert the output of the model to a 1D array
    model.add(Flatten())

    # Add a dropout layer with to avoid over-fitting
    model.add(Dropout(0.5))

    # Add a classification layer with num_classes output units,
    # followed by a softmax activation function
    model.add(Dense(num_classes, activation="softmax"))

    # Print a summary of the model architecture
    print(model.summary())

    return model
