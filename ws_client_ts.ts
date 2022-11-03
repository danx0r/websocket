var socket = new WebSocket("ws://localhost:1234");
socket.onopen = function (e) {
    console.log("[open] Connection established");
    console.log("Sending to server");
    socket.send("My name is danx0r");
};
socket.onmessage = function (event) {
    console.log("[message] Data received from server: ".concat(event.data));
    document.getElementById("message").innerHTML = event.data;
};
socket.onclose = function (event) {
    if (event.wasClean) {
        console.log("[close] Connection closed cleanly, code=".concat(event.code, " reason=").concat(event.reason));
    }
    else {
        // e.g. server process killed or network down
        // event.code is usually 1006 in this case
        console.log('[close] Connection died');
    }
};
socket.onerror = function (error) {
    console.log("[error] ".concat(error.message));
};
