from abc import ABC, abstractmethod


class Objects(ABC):
    @abstractmethod
    def get_figure(self):
        pass
