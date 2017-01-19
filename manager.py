import redis
import threading
import logging

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redis = redis.Redis(connection_pool=pool)

class Thread(threading.Thread):
    def __init__(self, r, channels, ws):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub()
        self.channels = [channels]
        self.channels.append("all")
        self.pubsub.subscribe(self.channels)
        self.ws = ws

    def run(self):
        for item in self.pubsub.listen():
            logging.debug(item)
            if item['type'] == 'message':
                self.ws.write_message(item['data'])
        logging.info("End {}".format(self.channels))

    def end(self):
        self.pubsub.unsubscribe(self.channels)

def create(username, ws):
    return Thread(redis, username, ws)
