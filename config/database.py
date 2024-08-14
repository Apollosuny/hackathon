import redis

hostname = '127.0.0.1'
port = 6379

r = redis.Redis(host=hostname, port=port)

print(r.ping())