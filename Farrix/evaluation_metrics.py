from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error, r2_score

class EvaluationMetrics:
    def mse(self, y_true, y_pred):
        return mean_squared_error(y_true, y_pred)
    def r2(self, y_true, y_pred):
        return r2_score(y_true, y_pred)
    def accuracy(self, y_true, y_pred):
        return accuracy_score(y_true, y_pred)

    def precision(self, y_true, y_pred):
        return precision_score(y_true, y_pred, average='macro')

    def recall(self, y_true, y_pred):
        return recall_score(y_true, y_pred, average='macro')

    def f1_score(self, y_true, y_pred):
        return f1_score(y_true, y_pred, average='macro')