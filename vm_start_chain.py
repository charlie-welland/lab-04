"""EE 250L Lab 04 Starter Code
Run vm_sub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("welland/pong")
    client.message_callback_add("welland/pong", on_message_from_ipinfo)

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

#Custom message callback.
def on_message_from_ipinfo(client, userdata, message):
   newNum = int(message.payload.decode())+1
   print("Custom callback  - Count: "+f"{newNum}")
   client.publish("welland/ping",f"{newNum}")
   time.sleep(1)




if __name__ == '__main__':
    #get IP address
    count = 0
    ip_address="172.20.10.5"

    """your code here"""
    #create a client object
    client = mqtt.Client()
    client.on_message = on_message
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in python. For example:
    
    `client.connect("eclipse.usc.edu", 11000, 60)` 
    
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    client.connect(host=ip_address, port=1883, keepalive=60)
    client.publish("welland/ping", count)
    
    client.loop_forever()
    
    

