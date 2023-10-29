# Auto-Image-CNN #Classification
 

![]()

## Business Goal

In this project, we will code and deploy an API for serving our own machine learning models. For this particular case, it will be a Convolutional Neural network for images. The main goal it will be develop a system that can receive images and return a prediction about the content of the image.

## About the data

![image](https://github.com/Dotto-Luis/Projects/assets/93018629/de2bc6b1-c152-4bcb-bf7a-c9aa017bc56f)

## Project Structure

Before starting to work, let's take a deep overview of the project structure and each module inside:

```
├── api
│   ├── Dockerfile
│   ├── app.py
│   ├── middleware.py
│   ├── views.py
│   ├── settings.py
│   ├── utils.py
│   ├── templates
│   │   └── index.html
│   └── tests
│       ├── test_api.py
│       └── test_utils.py
├── model
│   ├── Dockerfile
│   ├── ml_service.py
│   ├── settings.py
│   └── tests
│       └── test_model.py
├── stress_test
│   └── locustfile.py
├── docker-compose.yml
├── README.md
└── tests
    └── test_integration.py
```

Let's take a quick overview of each module:

- api: It has all the needed code to implement the communication interface between the users and our service. It uses Flask and Redis to queue tasks to be processed by our machine learning model.
    - `api/app.py`: Setup and launch our Flask api.
    - `api/views.py`: Contains the API endpoints. You must implement the following endpoints:
        - *upload_image*: Displays a frontend in which the user can upload an image and get a prediction from our model.
        - *predict*: POST method which receives an image and sends back the model prediction. This endpoint is useful for integration with other services and platforms given we can access it from any other programming language.
        - *feedback*: Endpoint used to get feedback from users when the prediction from our model is incorrect.
    - `api/utils.py`: Implements some extra functions used internally by our api.
    - `api/settings.py`: It has all the API settings.
    - `api/templates`: Here we put the .html files used in the frontend.
    - `api/tests`: Test suite.
- model: Implements the logic to get jobs from Redis and process them with our Machine Learning model. When we get the predicted value from our model, we must encode it on Redis again so it can be delivered to the user.
    - `model/ml_service.py`: Runs a thread in which it gets jobs from Redis, processes them with the model, and returns the answers.
    - `model/settings.py`: Settings for our ML model.
    - `model/tests`: Test suite.
- tests: This module contains integration tests so we can properly check our system's end-to-end behavior is expected.


## Requirement

- black==23.1.0
- flake8==6.0.0
- gdown==4.6.0
- isort==5.12.0
- Jupyter==1.0.0
- matplotlib==3.6.3
- numpy==1.24.2
- pandas==1.5.3
- pytest==7.2.1
- scikit-learn==1.2.1
- seaborn==0.12.2

```pip install -r requirements.txt```


## Project Origin

This project is based on a [Kaggle](https://www.kaggle.com/competitions/home-credit-default-risk/data) project.

I'd like to thank AnyoneAI for their contribution and inspiration in the development of this project.

# Sprint project 03
> Flask ML API

## The Business problem

Imagine that you work for a company that has a large collection of images and needs to automatically classify them into different categories. This task can be time-consuming and error-prone when done manually by human workers.

Your task is to develop a solution that can automatically classify images into over 1000 different categories using a Convolutional Neural Network (CNN) implemented in Tensorflow. Your solution will consist of a Web UI and a Python Flask API that serves the CNN.

The Web UI should allow users to upload an image and receive the predicted class for that image.

The Python Flask API should receive the uploaded image, preprocess it (e.g. resize, normalize), feed it into the CNN, and return the predicted class as a JSON object. The API should handle errors gracefully and provide informative error messages to the UI if something goes wrong.

You shouldn't worry for now about the TensorFlow CNN because we will use a pre-trained model for this problem. We provide you with a Jupyter notebook [here](https://drive.google.com/file/d/1ADuBSE4z2ZVIdn66YDSwxKv-58U7WEOn/view?usp=sharing) which shows how to load and run this model and hope will serve as a motivation for you to learn in-depth how these amazing models work during the next sprint!

## Technical aspects

To develop this solution you will need to have a proper working environment setup in your machine consisting of:
- Docker
- docker-compose
- VS Code or any other IDE of your preference
- Optional: Linux subsystem for Windows (WSL2)

Please make sure to carefully read the `ASSIGNMENT.md` file which contains detailed instructions about the code you have to complete to make the project run correctly.

The technologies involved are:
- Python is the main programming language
- Flask framework for the API
- HTML for the web UI
- Redis for the communication between microservices
- Tensorflow for loading the pre-trained CNN model
- Locust for doing the stress testing of your solution

## Installation

To run the services using compose:

```bash
$ cp .env.original .env
```

Only for mac M1 users:
- There is dockerfile for M1 macs model/Dockerfile.M1. This docker file downloads tensoflow compiled for M1
- Change docker-compose.yaml to use that docker file.
- Remove tensorflow for requirements.txt
- Remember change back docker-compose.yaml and requirements.txt in the submission.

Edit .env file and fill UID and GID env variables using command id -u and id -g.

```bash
$ docker-compose up --build -d
```

To stop the services:

```bash
$ docker-compose down
```

**Note: Why do I need to setup UID and GID?**

UID (User ID) and GID (Group ID) are used in Docker images to specify the user and group that should be used when running a container from the image.

When a Docker container is started, it runs as a specific user and group within the container's filesystem. By default, the user and group used in the container are the same as the ones on the host system that are running the container. However, this can lead to security issues because the container may have different permissions and access than the host system.

To avoid these issues, Docker provides the ability to specify a UID and GID when building a Docker image. This allows you to create a user and group within the container that has specific permissions and access. For example, you may want to create a user that has read-only access to certain directories or files within the container.

In addition to security, specifying a UID and GID can also help with the portability of Docker images. By using specific UIDs and GIDs, you can ensure that the container runs as expected across different host systems, even if those systems have different user and group configurations.

Overall, using UID and GID in a Docker image helps to ensure that containers are secure, portable, and operate with the appropriate permissions and access levels.

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

### 1. Modules

We make use of [multi-stage docker builds](https://docs.docker.com/develop/develop-images/multistage-build/) so we can have into the same Dockerfile environments for testing and also for deploying our service.

#### 1.1. Api

Run:

```bash
$ cd api/
$ docker build -t flask_api_test --progress=plain --target test .
```

You will only need to pay attention to the logs corresponding to the testing code which will look like this:

```bash
#10 [test 1/1] RUN ["pytest", "-v", "/src/tests"]
#10 sha256:707efc0d59d04744766193fe6873d212afc0f8e4b28d035a2d2e94b40826604f
#10 0.537 ============================= test session starts ==============================
#10 0.537 platform linux -- Python 3.8.13, pytest-7.1.1, pluggy-1.0.0 -- /usr/local/bin/python
#10 0.537 cachedir: .pytest_cache
#10 0.537 rootdir: /src
#10 0.537 collecting ... collected 4 items
#10 0.748
#10 0.748 tests/test_api.py::TestIntegration::test_bad_parameters PASSED           [ 25%]
#10 0.757 tests/test_api.py::TestEnpointsAvailability::test_feedback PASSED        [ 50%]
#10 0.769 tests/test_api.py::TestEnpointsAvailability::test_index PASSED           [ 75%]
#10 0.772 tests/test_api.py::TestEnpointsAvailability::test_predict PASSED         [100%]
#10 0.776
#10 0.776 ============================== 4 passed in 0.24s ===============================
#10 DONE 0.8s
```

You are good if all tests are passing.

#### 1.2. Model

Same as api, run:

```bash
$ cd model/
$ docker build -t model_test --progress=plain --target test .
```

### 2. Integration end-to-end

You must have the full pipeline running (see previous section) and the following Python libraries installed:

- [requests==2.28.1](https://requests.readthedocs.io/en/latest/)
- [pytest==7.1.2](https://docs.pytest.org/en/7.1.x/)

You can install them using the file `tests/requirements.txt` with:

```bash
$ pip3 install -r tests/requirements.txt
```

Then, from the project root folder run:

```
$ python tests/test_integration.py
```

If the output looks like this, then the integration tests are passing:

```bash
.
----------------------------------------------------------------------
Ran 2 tests in 0.299s

OK
```

If you want to learn more about testing Python code, please read:
- [Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)
- [The Hitchhiker’s Guide to Python: Testing Your Code](https://docs.python-guide.org/writing/tests/)

