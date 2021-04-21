import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def predict(self):
        self.client.post("/predict", json={"day":"12", "total":"123456"})
