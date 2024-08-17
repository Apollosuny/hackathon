import redis

hostname = "127.0.0.1"
port = 6379


def connect_redis():
    return redis.Redis(hostname, port)
