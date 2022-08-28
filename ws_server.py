import asyncio
import websockets

async def response(websocket, path):
	message = await websocket.recv()
	print(f"We got the message from the client: {message}")
	await websocket.send(f"I can confirm I got your message: {message}")

host, port = "localhost", 1234
start_server = websockets.serve(response, host, port)
print (f"Serving on {host}:{port}")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
