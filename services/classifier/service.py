import pickle

from sklearn.neighbors import KNeighborsClassifier
from sentence_transformers import SentenceTransformer

from .interface import Category
from .interface import IClassifier
from .interface import Text
from .settings import ClassifierSettings
from ..base_settings import BASE_PATH


class Classifier(IClassifier):
    def __init__(self):
        settings = ClassifierSettings()

        self.model_feature_extractor = SentenceTransformer(settings.feature_extractor)
        with open(f'{BASE_PATH}/services/classifier/models/{settings.classifier}.pickle', 'rb') as f:
            self.model_classifier: KNeighborsClassifier = pickle.load(f)

    def classify_many(self, data: list[Text]) -> list[Category]:
        features = self.model_feature_extractor.encode(data)
        predictions = self.model_classifier.predict(features)
        categories = [Category(prediction) for prediction in predictions]

        return categories
