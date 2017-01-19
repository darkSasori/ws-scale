import tornado.wsgi
import os
import logging
from wsgiref.simple_server import make_server
import handlers
import settings
import redis

log = logging.getLogger()
log.setLevel(logging.DEBUG)

routes = [
    (r'/ws/(.*)', handlers.WebSocket),
    (r'/', handlers.Main),
]

application = tornado.web.Application(routes, **settings.settings)

if __name__ == '__main__':
    ip   = 'localhost'
    port = int(os.getenv("WS_SCALE_PORT", 8888))
    application.listen(port)
    print("Listen: %s:%d" %(ip,port))
    tornado.ioloop.IOLoop.instance().start()
    publisher.conn.close()
