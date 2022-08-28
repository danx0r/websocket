from browser import document
from browser.websocket import WebSocket
from browser import console
# print ("brython")

socket = WebSocket("ws://localhost:1234")

def onopen(e):
    console.log("[open] Connection established")
    console.log("Sending to server")
    socket.send("My name is danx0r")

socket.onopen = onopen


def onmessage(e):
    console.log(f"[message] Data received from server: {e.data}")
    document["message"].innerHTML = e.data

socket.onmessage = onmessage


def onclose(e):
    if (e.wasClean):
        console.log(f"[close] Connection closed cleanly, code={e.code} reason={e.reason}")
    else:
        # // e.g. server process killed or network down
        # // event.code is usually 1006 in this case
        console.log('[close] Connection died')

socket.onclose = onclose


def onerror(error):
    console.log(f"[error] {error.message}")

socket.onerror = onerror
