import websocket as wsc
wc = wsc.create_connection("ws://127.0.0.1:1234")
wc.send("AAAAA")
print (wc.recv())
