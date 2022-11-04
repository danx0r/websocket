#python:
#term1:
python3 ws_server.py
#term 2:
python3 ws_client.py

#python non-async (note websocket-client package not websockets):
#python:
#term1:
python3 ws_server.py
#term 2:
python3 ws_client_no_async.py

#javascript:
#term1:
sh serve.sh
#term2:
python3 ws_server.py
#browser:
http://localhost:8000/browser.html

#Brython:
#term1:
sh serve.sh
#term2:
python3 ws_server.py
#browser:
http://localhost:8000/brython.html

#typescript:
tsc ws_client_ts.ts
#generates ws_client_ts.js
#term1:
sh serve.sh
#term2:
python3 ws_server.py
#browser:
http://localhost:8000/typescript.html
