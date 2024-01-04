from .database import DataBaseMethods


class BestScore:
    def __init__(self):
        self.variable_name = 'best_score'
        self.current_best_score = self.get_best_score()


    def get_best_score(self) -> float:
        """Returns the best user score so far"""
        try:
            # if the score is found: set it to current best score and return
            best_score = int(DataBaseMethods.get_value(redis_variable_name=self.variable_name))
            self.current_best_score = best_score
            return self.current_best_score
        except ValueError:
            # if it's not found set 0 to database and return it
            self.current_best_score = 0
            self.save_new_best_score(new_score=self.current_best_score)
            return self.current_best_score

    def save_new_best_score(self, new_score):
        if new_score > self.current_best_score:
            DataBaseMethods.set_value(redis_variable_name=self.variable_name, value=new_score)
