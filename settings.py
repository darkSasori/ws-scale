import os
import redis

settings = dict(
    static_path=os.path.join(os.getcwd(), 'static'),
    template_path=os.path.join(os.getcwd(), 'templates'),
    autoreload=True,
    debug=True,
    redis_uri="redis://localhost:6379/0"
)
