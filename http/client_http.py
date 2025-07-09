import requests
import time

URL = 'http://127.0.0.1:8081/'

while True:
    msg = "Hello"
    r = requests.post(URL, data=msg)
    print("Sent:", msg, "Status:", r.status_code)
    time.sleep(1)
