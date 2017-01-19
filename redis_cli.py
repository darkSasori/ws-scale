import redis
import time
import sys
from settings import settings

if __name__ == "__main__":
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)

    for line in sys.stdin:
        print("Publish: {}".format(line))
        r.publish('teste', line)
