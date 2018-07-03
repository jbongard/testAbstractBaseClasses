from abc import ABC, abstractmethod

class Chat(ABC):

    def __init__(self, message):

        self.message = message

        super().__init__()

    @abstractmethod
    def Handle(self):

        pass
