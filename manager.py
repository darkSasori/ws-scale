import logging

class Client(object):
    def __init__(self, username):
        self.username = username
        self.connections = []

    def add(self, ws):
        if ws in self.connections:
            return False
        self.connections.append(ws)
        logging.info("%s: %d", self.username, len(self.connections))

    def remove(self, ws):
        if ws not in self.connections:
            return False
        self.connections.remove(ws)
        logging.info("%s: %d", self.username, len(self.connections))

    def send(self, msg):
        [ ws.write_message(msg) for ws in self.connections ]

class Manager(object):
    def __init__(self):
        self.clients = {}

    def add(self, username, ws):
        try:
            client = self.clients[username]
        except:
            self.clients[username] = Client(username)
            client = self.clients[username]

        client.add(ws)
        logging.info("Clients: %d", len(self.clients))

    def remove(self, username, ws):
        try:
            self.clients[username].remove(ws)
        except:
            pass

    def send(self, user_to, user_from, msg):
        try:
            self.clients[user_to].send(msg)
            self.clients[user_from].send(msg)
        except:
            pass

    def sendAll(self, msg):
        [ cli.send(msg) for key, cli in self.clients.items() ]

manager = Manager()
