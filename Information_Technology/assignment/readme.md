# Sprint Project 04
> Vehicle classification from images

## The Business problem

Imagine a company that has a large inventory of used cars and wants to create a website or a mobile app to make it easier for customers to search and find the exact car they are looking for. One way to improve the user experience would be to allow customers to search for cars by make and model. However, manually entering this information for every car in the inventory could be time-consuming and error-prone.

Using a machine learning model capable of classifying vehicle make and model from images, the company could automatically extract this information from pictures of the cars. This would make it faster and more accurate to input the information, allowing customers to easily search and filter cars by make and model. This would not only improve the customer experience but also save the company time and resources. Additionally, the model could be used to automatically identify and categorize new cars as they come into the inventory.

Now, image you are working for that company as a Machine Learning Engineer and are in charge of creating such model. For the initial proof-of-concept, the Data team collected and labelled pictures for 25 different cars. Your task will be to train a model able to classify those vehicles with a high accuracy (over 80% on the testing dataset).

This is a Multi-class Classification task: we want to predict, given a picture of a vehicle, which of the possible 25 classes is the correct vehicle make-model.

## About the data

The dataset is composed of JPG images, already stored in folders containing the label (vehicle make-model), separated in train and test sets.

You don't have to worry about downloading the data, it will be automatically downloaded from the `AnyoneAI - Sprint Project 04.ipynb` notebook in `Section 1 - Getting the data`.

## Technical aspects

To develop this Machine Learning model you will have to primary interact with the Jupyter notebook provided, called `AnyoneAI - Sprint Project 04.ipynb`. This notebook will guide you through all the steps you have to follow and the code you have to complete in the different parts of the project, also marked with a `TODO` comment.

The only file having `TODO`s that will require you to add your own code is `src/models.py`.

The technologies involved are:
- Python as the main programming language
- Tensorflow and keras for building features and training ML models
- Matplotlib for the visualizations
- Jupyter notebooks to make the experimentation in an interactive way

## Training on GPUs

Note for some of the models you will use in this project, the most efficient way to train them is using GPUs.

Currently one the best free options to get a GPU you can use for a couple of hours is Google Colab. To get access to GPUs trhough Colab, follow the steps below:
- First, create a Google account if you don't already have one.
- Go to the Google Colab website and sign in using your Google account credentials.
- Open Google Drive service and upload your project code (make sure you've implemented all the TODOs and your code passes the unit tests provided).
- Open the folder with you code from Google Drive, right click on the notebook `AnyoneAI - Sprint Project 04.ipynb` and select "Open with:" -> "Google Colaboratory"
- In the new notebook, click on "Runtime" in the top menu and select "Change runtime type".
- Select "GPU" as the hardware accelerator, which will allow for faster model training.

**Important Note: ** In the version of Colab that is free of charge notebooks can run for at most 12 hours, depending on availability and your usage patterns.

## Installation

### Option A. Virtual environment

A `requirements.txt` file is provided with all the needed Python libraries for running this project. For installing the dependencies just run:

```console
$ pip install -r requirements.txt
```

*Note:* We encourage you to install those inside a virtual environment.

### Option B. Using Docker

You can use `Docker` to install all the needed packages and libraries easily. Two Dockerfiles are provided for both CPU and GPU support.

- **CPU:**

```bash
$ docker build -t sp_04 --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -f docker/Dockerfile .
```

- **M1:**

```bash
$ docker build -t sp_04 --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -f docker/Dockerfile.M1 .
```

- **GPU:**

```bash
$ docker build -t sp_04 --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -f docker/Dockerfile_gpu .
```

#### Run Docker

- **CPU:**

```bash
$ docker run --rm --net host -it \
    -v $(pwd):/home/app/src \
    --workdir /home/app/src \
    sp_04 \
    bash
```

- **GPU:**

```bash
$ docker run --rm --net host --gpus all -it \
    -v $(pwd):/home/app/src \
    --workdir /home/app/src \
    sp_04 \
    bash
```

## Code Style

Following a style guide keeps the code's aesthetics clean and improves readability, making contributions and code reviews easier. Automated Python code formatters make sure your codebase stays in a consistent style without any manual work on your end. If adhering to a specific style of coding is important to you, employing an automated to do that job is the obvious thing to do. This avoids bike-shedding on nitpicks during code reviews, saving you an enormous amount of time overall.

We use [Black](https://black.readthedocs.io/) and [isort](https://pycqa.github.io/isort/) for automated code formatting in this project, you can run it with:

```console
$ isort --profile=black . && black --line-length 88 .
```

Wanna read more about Python code style and good practices? Please see:
- [The Hitchhiker’s Guide to Python: Code Style](https://docs.python-guide.org/writing/style/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

## Tests

We provide unit tests along with the project that you can run and check from your side the code meets the minimum requirements of correctness needed to approve. To run just execute:

```console
$ pytest tests/
```

If you want to learn more about testing Python code, please read:
- [Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)
- [The Hitchhiker’s Guide to Python: Testing Your Code](https://docs.python-guide.org/writing/tests/)