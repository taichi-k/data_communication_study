import requests
import time

URL = 'https://127.0.0.1:8081/'

while True:
    msg = "Hello"
    # Disable SSL verification for testing purposes
    r = requests.post(URL, data=msg, verify=False)
    print("Sent:", msg, "Status:", r.status_code)
    time.sleep(1)
