from .model import Model
from sklearn.tree import DecisionTreeClassifier as SkDecisionTreeClassifier
from sklearn.metrics import accuracy_score

class DecisionTreeClassifier(Model):
    def __init__(self, max_depth=None, min_samples_split=2, random_state=42):
        self.model = SkDecisionTreeClassifier(max_depth=max_depth,
                                              min_samples_split=min_samples_split,
                                              random_state=random_state)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy