import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix

class Visualization:
    def plot_data(self, X, y):
        # Assuming X has two features for visualization purposes
        plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y)
        plt.show()

    def plot_model_performance(self, model, X_test, y_test):
        plot_confusion_matrix(model, X_test, y_test)
        plt.show()

    def plot_learning_curve(self, train_sizes, train_scores, test_scores):
        plt.plot(train_sizes, train_scores, 'o-', label='Training Scores')
        plt.plot(train_sizes, test_scores, 'o-', label='Test Scores')
        plt.xlabel('Training Examples')
        plt.ylabel('Score')
        plt.legend()
        plt.show()