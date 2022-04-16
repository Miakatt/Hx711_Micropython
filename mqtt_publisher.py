from umqtt.robust import MQTTClient
import time

#mqttBroker = "mqtt.eclipseprojects.io"
client = MQTTClient('32d222d-d32w2d', 'mqtt.eclipseprojects.io')
client.connect()

def publish(data):
    client.publish("Strain", data)
    