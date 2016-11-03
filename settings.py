import os
import redis

settings = dict(
    static_path=os.path.join(os.getcwd(), 'static'),
    template_path=os.path.join(os.getcwd(), 'templates'),
    autoreload=True,
    debug=True,
    redis_host=redis.ConnectionPool(host="localhost", port=6379, db=0)
)
