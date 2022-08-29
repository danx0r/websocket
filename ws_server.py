import asyncio
import websockets

state = [0]

async def response(websocket, path):
    message = await websocket.recv()
    state[0] += 1
    print(f"state: {state[0]} Message from client: {message}")
    await websocket.send(f"state: {state[0]} Confirming message: {message}")


async def work():
    while 1:
        state[0] += 1
        print (f"State: {state[0]}")
        await asyncio.sleep(1)

worktask = asyncio.ensure_future(work())

host, port = "localhost", 1234
start_server = websockets.serve(response, host, port)
print (f"Serving on {host}:{port}")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
