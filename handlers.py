import tornado.web
import tornado.websocket
import settings
import re
import manager

class Main(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class WebSocket(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self, username):
        self.username = username
        self.thread = manager.create(self.username, self)
        print(self.thread)
        self.thread.start()

    def on_message(self, msg):
        m = re.search('(\w+):(.*)', msg)
        msg = "%s => %s" % (self.username, msg)
        try:
            manager.redis.publish(m.group(1), msg)
            manager.redis.publish(self.username, msg)
        except:
            manager.redis.publish("all", msg)

    def on_close(self):
        self.thread.end()
