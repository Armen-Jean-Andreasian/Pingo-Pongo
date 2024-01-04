import redis


class RedisDbBase:
    @classmethod
    def create_connection(cls):
        redis_client = redis.Redis(host='localhost', port=6379, db=0)
        return redis_client

    @classmethod
    def close_connection(cls, client: redis.Redis):
        client.close()


class RedisDbMethods(RedisDbBase):
    @classmethod
    def get_value(cls, redis_variable_name: str):
        redis_client = cls.create_connection()
        try:
            result = redis_client.get(name=redis_variable_name)
            cls.close_connection(client=redis_client)
            return result
        except redis.exceptions.RedisError:
            cls.set_value(redis_variable_name=redis_variable_name, value=0)
            result = redis_client.get(name=redis_variable_name)
            cls.close_connection(client=redis_client)
            return result


    @classmethod
    def set_value(cls, redis_variable_name: str, value):
        redis_client = cls.create_connection()
        try:
            redis_client.set(name=redis_variable_name, value=value)
            cls.close_connection(client=redis_client)
        except redis.exceptions.RedisError:
            cls.close_connection(client=redis_client)
            raise ValueError('Variable not found')


class RedisBestScore:
    def __init__(self):
        self.variable_name = 'best_score'
        self.current_best_score = self.get_best_score()

    def __set_zero(self):
        # if key is not found sets the key to 0 and returns it
        self.current_best_score = 0
        self.save_new_best_score(new_score=self.current_best_score)
        return self.current_best_score

    def get_best_score(self) -> float:
        """Returns the best user score so far"""
        try:
            # if the score is found: set it to current best score and return
            result = RedisDbMethods.get_value(redis_variable_name=self.variable_name)
            if result is not None:
                best_score = int(result)
                self.current_best_score = best_score
                return self.current_best_score
            else:
                # if it's not found set 0 to database and return it
                return self.__set_zero()
        except Exception:
            return self.__set_zero()


    def save_new_best_score(self, new_score):
        if new_score > self.current_best_score:
            RedisDbMethods.set_value(redis_variable_name=self.variable_name, value=new_score)



if __name__ == '__main__':
    RedisDbMethods.set_value(redis_variable_name="temp", value=0)
