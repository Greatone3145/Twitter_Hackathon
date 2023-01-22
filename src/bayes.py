from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
import numpy

class Bayes_AI:
    # Supervised learning classifier that uses Gaussian Naive Bayes
    X, y, X_train, X_test, y_train, y_test = 0, 0, 0, 0, 0, 0
    classifier = None

    def __init__(self, binaryDataset, infoDataset, test_size_percentage = 0.50):

        self.X = numpy.array(infoDataset)
        self.y = numpy.array(binaryDataset)
        print(self.y)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size= test_size_percentage, random_state=0)
        self.classifier = GaussianNB()

    def predicter(self):
        sc_X = StandardScaler()
        self.X_train = sc_X.fit_transform(self.X_train)
        self.X_test = sc_X.fit_transform(self.X_test)
        self.classifier.fit(self.X_train, self.y_train)
        return self.classifier.predict(self.X_test)

    def successPrediction(self):
        temp = self.predicter()
        prediction = numpy.ndarray.tolist(temp)
        return prediction.count(0) / len(prediction)
