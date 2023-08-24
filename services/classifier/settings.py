from services.base_settings import Settings


class ClassifierSettings(Settings):
    feature_extractor: str
    classifier: str

    class Config:
        env_prefix = 'classifier_'
