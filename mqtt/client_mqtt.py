import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("127.0.0.1", 1883)
while True:
    msg = "Hello"
    client.publish("test/topic", msg)
    print("Sent:", msg)
    time.sleep(1)
