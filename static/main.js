var ws = undefined;

function connect() {
    var username = document.getElementById("username").value;
    if (username === "") {
        alert("Set username before connect");
        return;
    }

    if (ws !== undefined) {
        ws.close();
    }
    var url = "ws://"+location.hostname+":"+location.port+"/ws/"+username;

    ws = new WebSocket(url);
    ws.onopen = function(event) {
        console.log("connected");
    }
    ws.onmessage = function(msg) {
        document.getElementById("msgList").innerHTML += msg.data+"<br />";
    };
}

function keyPressed(element) {
    if (event.keyCode !== 13) {
        return;
    }

    if (ws === undefined) {
        alert("Not connected");
        return;
    }
    ws.send(element.value);
    element.value = "";
}
