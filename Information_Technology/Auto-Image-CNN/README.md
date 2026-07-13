# Auto Image CNN — Flask ML API #DeepLearning

![Cover](https://github.com/Dotto-Luis/Projects/blob/main/Information_Technology/Auto-Image-CNN/images/cover.png?raw=true)

## Table of Contents

1. [Business Goal](#business-goal)
2. [About the Data](#about-the-data)
3. [Usage Examples](#usage-examples)
4. [Project Structure](#project-structure)
5. [Requirements](#requirements)
6. [Tests](#tests)
7. [Contributing](#contributing)
8. [License](#license)
9. [Project Origin](#project-origin)

---

## 1. Business Goal

Companies with large image collections need to automatically classify images into categories — manually doing so is time-consuming and error-prone. This project builds a solution that classifies images into over 1,000 categories using a pre-trained Convolutional Neural Network (CNN) served via a Python Flask API and a Web UI.

- The **Web UI** allows users to upload an image and receive the predicted class.
- The **Flask API** preprocesses the image, runs inference, and returns the result as JSON.
- **Redis** is used for asynchronous communication between microservices.

Tech stack: Python · Flask · TensorFlow · Redis · Docker · Locust

---

## 2. About the Data

This project uses a pre-trained ImageNet model (1,000+ categories). No custom dataset is required — the model is loaded from a pre-trained checkpoint provided via Google Drive.

---

## 3. Usage Examples

Start all services:

```bash
cp .env.original .env
# Edit .env with your UID and GID (run: id -u && id -g)
docker-compose up --build -d
```

Stop services:

```bash
docker-compose down
```

Then navigate to `http://localhost` to upload images and get predictions.

---

## 4. Project Structure

<details>
  <summary>📂 Expand for Project Structure</summary>

```console
├── api/
│   ├── Dockerfile
│   └── src/
│       ├── app.py
│       └── tests/
├── model/
│   ├── Dockerfile
│   ├── Dockerfile.M1
│   └── ml_service.py
├── stress_test/
│   └── locustfile.py
├── tests/
│   ├── requirements.txt
│   └── test_integration.py
├── ASSIGNMENT.md
├── docker-compose.yml
├── .env.original
└── README.md
```
</details>

---

## 5. Requirements

```bash
cp .env.original .env
docker-compose up --build -d
```

Dependencies (installed via Docker):
- Python · Flask · TensorFlow · Redis · Locust

For integration tests:
```bash
pip install -r tests/requirements.txt
```

---

## 6. Tests

**Unit tests (API):**

```bash
cd api/
docker build -t flask_api_test --progress=plain --target test .
```

**Unit tests (Model):**

```bash
cd model/
docker build -t model_test --progress=plain --target test .
```

**Integration tests** (requires services running):

```bash
python tests/test_integration.py
```

---

## 7. Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## 8. License

This project is licensed under the MIT License.

---

## 9. Project Origin

Based on an AnyoneAI sprint project focused on deploying CNN models as production-ready Flask microservices.
