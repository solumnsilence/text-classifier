from abc import ABC
from abc import abstractmethod
from typing import NewType

Category = NewType('Category', str)
Text = NewType('Category', str)


class IClassifier(ABC):

    @abstractmethod
    def classify_many(self, data: list[Text]) -> list[Category]:
        pass

    def classify(self, text: Text) -> Category:
        """Wrapper to simplify the usage"""

        # better to make a queue and process classification in batches
        return self.classify_many([text])[0]
