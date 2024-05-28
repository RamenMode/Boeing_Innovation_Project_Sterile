import tensorflow as tf
import tensorflow_hub as hub


class Embedder():
    def __init__(self):
        module_url = "https://www.kaggle.com/models/google/universal-sentence-encoder/frameworks/tensorFlow2/variations/universal-sentence-encoder/versions/2?tfhub-redirect=true"
        self.model = hub.load(module_url)
        print("module %s loaded" % module_url)

    def embed(self, plain_text):
        print(f'plain_test: {plain_text}')
        em_text = self.model(plain_text)
        return em_text