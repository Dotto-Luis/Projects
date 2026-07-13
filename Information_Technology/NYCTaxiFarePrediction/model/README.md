## Machine Learning Model

This folder contains all the resources to build, train, and deploy the ML models for the project.

The project uses mainly 2 ML models: fare amount and trip duration. 

Although, there is a previous step needed, to estimte the average speed in hour.
It's an estimation of hourly speed based on different data from the other two models.
This provides an important feature for the ML models that depends on the hour of the trip.

## Generate ML resources for the Taxi App and Docker

The taxi app requires ML models and artifacts to run the pipeline workflow.

1) Install requirements with `pip3 install -r requirements.txt`

2) Open the Jupyter notebook `avg_speed.ipynb`. This will generate a model artifact for the average speed feature.

3) Run the Jupyter notebook `model_train.ipynb` to generate the machine learning models weights and save in disk.

At the end of this, you should see these files in the model folder:
* lgbm_model_fa.model
* lgbm_model_td.model
* avg_speed_dict.model

## How to run in Docker

To test the model locally with Docker, and have the models weights, first go to the previous section and follow the instructions.

Run docker app:

`docker build -t mlapp .`

`docker run -p 5000:5000 mlapp`

The go to your browser and type:

`http://127.0.0.1:5000/test`

You should see something like:

```
{
  "fare_amount": 21.37,
  "status": [
    "OK",
    200
  ],
  "trip_duration": 26
}
```