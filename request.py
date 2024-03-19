import requests

def send_integration_request(url, payload):
    response = requests.post(url, json=payload)
    
    print(f"Integration request status code: {response.status_code}")
    print("Integration request response:")
    print(response.text)

mock_url = 'https://jsonplaceholder.typicode.com/posts'
sample_payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
send_integration_request(mock_url, sample_payload)
