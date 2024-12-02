from locust import HttpUser, task, between
import csv
import random

def load_urls(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        return [row[1] for row in reader if row] 

URLS = load_urls("urldata.csv")

class PhishingDetectorUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_predict(self):
        url = random.choice(URLS)
        payload = {"url": url}
        self.client.post("/predict", json=payload)