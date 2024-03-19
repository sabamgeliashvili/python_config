import requests
import time

def monitor_service(url, threshold=5):
    while True:
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Service is down! Status code: {response.status_code}")
            
            break
        else:
            print("Service is up and running.")
        
        time.sleep(threshold)

sample_service_url = 'https://www.example.com'
monitor_service(sample_service_url)
