import json
import os
import time

import numpy as np
import redis
import settings
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import decode_predictions, preprocess_input
from tensorflow.keras.preprocessing import image

# TODO
# Connect to Redis and assign to variable `db``
# Make use of settings.py module to get Redis settings like host, port, etc.
db = redis.Redis(host=settings.REDIS_IP, port=settings.REDIS_PORT, db=settings.REDIS_DB_ID)


# TODO
# Load your ML model and assign to variable `model`
# See https://drive.google.com/file/d/1ADuBSE4z2ZVIdn66YDSwxKv-58U7WEOn/view?usp=sharing
# for more information about how to use this model.
model = ResNet50(include_top=True, weights="imagenet")



def predict(image_name):
    """
    Load image from the corresponding folder based on the image name
    received, then, run our ML model to get predictions.

    Parameters
    ----------
    image_name : str
        Image filename.

    Returns
    -------
    class_name, pred_probability : tuple(str, float)
        Model predicted class as a string and the corresponding confidence
        score as a number.
    """
    class_name = None
    pred_probability = None

    # TODO
    img_path = os.path.join(settings.UPLOAD_FOLDER, image_name)
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)

    predictions = model.predict(img)
    decoded_predictions = decode_predictions(predictions, top=1)[0]
    class_name = decoded_predictions[0][1]
    pred_probability = round(decoded_predictions[0][2],4)

    return class_name, pred_probability


def classify_process():
    """
    Loop indefinitely asking Redis for new jobs.
    When a new job arrives, takes it from the Redis queue, uses the loaded ML
    model to get predictions and stores the results back in Redis using
    the original job ID so other services can see it was processed and access
    the results.

    Load image from the corresponding folder based on the image name
    received, then, run our ML model to get predictions.
    """
    while True:
        # brpop blocks until a job is available and returns a
        # (queue_name, message) tuple — the message is the JSON job payload
        # pushed by the API: {"id": str, "image_name": str}
        _, msg = db.brpop(settings.REDIS_QUEUE)

        # A single bad job (corrupt image, unsupported format, malformed
        # payload) must never kill the service: report the error back to
        # the API and keep consuming the queue.
        try:
            job = json.loads(msg)
            job_id = job["id"]
            image_name = job["image_name"]
        except (ValueError, KeyError) as e:
            print(f"Skipping malformed job payload: {e}")
            continue

        try:
            class_name, pred_probability = predict(image_name)
            result = {
                "prediction": class_name,
                # numpy floats are not JSON serializable — cast to native float
                "score": float(pred_probability),
            }
        except Exception as e:
            print(f"Prediction failed for '{image_name}': {e}")
            result = {
                "prediction": f"ERROR: could not process image ({type(e).__name__})",
                "score": 0.0,
            }

        db.set(job_id, json.dumps(result))

        # Sleep for a bit
        time.sleep(settings.SERVER_SLEEP)


if __name__ == "__main__":
    # Now launch process
    print("Launching ML service...")
    classify_process()
