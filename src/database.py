import redis


class DataBase:
    @classmethod
    def create_connection(cls):
        redis_client = redis.Redis(host='localhost', port=6379, db=0)
        return redis_client

    @classmethod
    def close_connection(cls, client: redis.Redis):
        client.close()


class DataBaseMethods(DataBase):
    @classmethod
    def get_value(cls, redis_variable_name: str):
        redis_client = cls.create_connection()
        try:
            result = redis_client.get(name=redis_variable_name)
            cls.close_connection(client=redis_client)
            return result
        except redis.exceptions.RedisError:
            cls.close_connection(client=redis_client)
            raise ValueError('Variable not found')

    @classmethod
    def set_value(cls, redis_variable_name: str, value):
        redis_client = cls.create_connection()
        try:
            redis_client.set(name=redis_variable_name, value=value)
            cls.close_connection(client=redis_client)
        except redis.exceptions.RedisError:
            cls.close_connection(client=redis_client)
            raise ValueError('Variable not found')


if __name__ == '__main__':
    DataBaseMethods.set_value(redis_variable_name="temp", value=0)
