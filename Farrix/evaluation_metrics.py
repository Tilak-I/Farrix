from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class EvaluationMetrics:
    def accuracy(self, y_true, y_pred):
        return accuracy_score(y_true, y_pred)

    def precision(self, y_true, y_pred):
        return precision_score(y_true, y_pred, average='macro')

    def recall(self, y_true, y_pred):
        return recall_score(y_true, y_pred, average='macro')

    def f1_score(self, y_true, y_pred):
        return f1_score(y_true, y_pred, average='macro')