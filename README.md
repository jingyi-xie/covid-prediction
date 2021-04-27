# IDS721 Final Project: Covid Prediction

In this project, we built a **machine learning** model to predict the number of Covid positive cases and deployed it on **Flask**. The **Flask** app is deployed on **Google App Engine** and can be accessed through a public url. We also verified the elastic scale-Up performance via Load Test with **Locust**.
* Application Deployed on: https://covid-prediction-311000.uc.r.appspot.com
* ML Framework: Sklearn
* Platform: Flask + Google App Engine
* Load Test Framework: Locust
* Dataset: https://raw.githubusercontent.com/jingyi-xie/covid-prediction/main/national-history-update.csv  

Here is an image of the frontend website:  
![CleanShot 2021-04-20 at 22 06 08](https://user-images.githubusercontent.com/49466651/115486455-ad015480-a224-11eb-850e-4a5913e8c605.png)
Here is an image of the load test result:  
![CleanShot 2021-04-20 at 21 42 03](https://user-images.githubusercontent.com/49466651/115485025-e84e5400-a221-11eb-8285-4a62499597d4.png)

## How to build from scratch
To deploy this Ml model and flask app on Google Cloud Platform, you can follow these steps:

### Set up project
Launch Google Cloud Platform, create a new project. Change your current project to it and activate Cloud Shell.  
Git clone this repository to your GCP local and cd into it.  

### Run this app locally
Create a virtual environment and activate it. (To deactivate it, run ```deactivate```).  
```
make set-up
source ~/.covid_venv/bin/activate
```
Install the required packages.  
```
make install
```
Run this app, the flask app will be running on http://127.0.0.1:8080/.  
```
python3 main.py
```
You can test it from the frontend or send a POST request to this app through a bash script.  
### Deployed this app on GCP

### Test with locust

### Done!
