#!/usr/bin/python3

import websocket
import json

# Define the WebSocket URL
ws_url = "ws://bagel.htb:5000/"

# Define the WebSocket connection callback functions
def on_open(ws):
    # Create a dictionary containing the request parameters
    order = {"ReadOrder": "orders.txt"}

    # Convert the dictionary to a JSON-encoded string
    data = json.dumps(order)

    # Send the message to the WebSocket server
    ws.send(data)

def on_message(ws, message):
    # Print the received message
    print(json.loads(message)['ReadOrder'])

# Create a new WebSocket object
ws = websocket.WebSocketApp(ws_url,
                            on_open=on_open,
                            on_message=on_message)

# Connect to the WebSocket server and start the event loop
ws.run_forever()

