import sklearn
import sklearn.model_selection
import sklearn.svm

class Classifier():
    def __init__(self, name):
        self.svc = sklearn.svm.SVC(random_state=42)
        self.name = name

    def split_data(self, input_data, output_data):
        self.X_train, self.X_test, self.y_train, self.y_test = sklearn.model_selection.train_test_split(input_data, output_data, test_size = 0.3, random_state=42)

    def train(self, input_train=None, output_train=None):
        if input_train is None:
            input_train = self.X_train
        if output_train is None:
            output_train = self.y_train

        self.svc.fit(input_train, output_train)

    def test(self, input_test=None, output_test=None):
        if input_test is None:
            input_test = self.X_test
        if output_test is None:
            output_test = self.y_test
        accuracy = self.svc.score(input_test, output_test)
        print(f"tested accuracy = {accuracy * 100}%")

    def predict(self, input_predict):
        prediction = self.svc.predict(input_predict)
        return prediction

    


