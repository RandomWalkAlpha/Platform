import redis


class RedisController:
    """
    A controller class for redis managing
    """
    def __init__(self, host='127.0.0.1', port=6379, password=None):
        self.pool = redis.ConnectionPool(host=host, port=port, password=password, decode_responses=True)
        self.connection = redis.Redis(connection_pool=self.pool)

    def put(self, name, value):
        self.connection.set(name, value)

    def get(self, name):
        self.connection.get(name)

