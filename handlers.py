import tornado.web
import tornado.websocket
import settings
import manager
import re

class Main(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class WebSocket(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self, username):
        self.username = username
        self.manager = manager.manager
        self.manager.add(self.username, self)

    def on_message(self, msg):
        m = re.search('(\w+):(.*)', msg)
        msg = "%s => %s" % (self.username, msg)
        try:
            self.manager.send(m.group(1), self.username, msg)
        except:
            self.manager.sendAll(msg)

    def on_close(self):
        self.manager.remove(self.username, self)
