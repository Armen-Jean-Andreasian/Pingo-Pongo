import json


class Database:
    db_path = 'src/data/database.json'
    key = "best_score"

    @classmethod
    def get_score(cls):
        with open(cls.db_path, "r") as jsonfile:
            content: dict = json.load(jsonfile)
            return content.get(cls.key, 0)

    @classmethod
    def update_score(cls, new_score):
        with open(cls.db_path, "w") as jsonfile:
            json.dump({cls.key: new_score}, jsonfile, indent=2)
        return None


class UserBestScore:
    __slots__ = ['current_best_score']

    def __init__(self):
        self.current_best_score = Database.get_score()

    def get_best_score(self) -> float:
        return self.current_best_score

    def save_new_best_score(self, new_score):
        if new_score > self.current_best_score:
            Database.update_score(new_score)
            self.current_best_score = new_score
        return self

