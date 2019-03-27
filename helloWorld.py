#!/usr/bin/env python3
from hermes_python.hermes import Hermes

MQTT_ADDR = "localhost:1883"        # Specify host and port for the MQTT broker

def subscribe_zimmer_callback(hermes, intent_message):    # Defining callback functions to handle an intent that asks for the weather.
     print("Parsed intent : {}".format(intent_message.intent.intent_name))
     result_sentence = "Hallo Welt"
     current_session_id = intent_message.session_id
     hermes.publish_end_session(current_session_id, result_sentence)

with Hermes(MQTT_ADDR) as h: # Initialization of a connection to the MQTT broker
    h.subscribe_intent("Zimmer", Zimmer) \  # Registering callback functions to handle the searchWeatherForecast intent
         .start()
    # We get out of the with block, which closes and releases the connection