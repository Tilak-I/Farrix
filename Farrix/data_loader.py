import pandas as pd
from sklearn.model_selection import train_test_split
from skfeature.function.similarity_based import cfs

class DataLoader:
    def __init__(self, data_source, target_column, feature_selection=True):
        self.data_source = data_source
        self.target_column = target_column
        self.feature_selection = feature_selection

    def load_data(self):
        # Load data from CSV file
        data = pd.read_csv(self.data_source)
        return data

    def preprocess_data(self, data):
        # Handle missing values by dropping rows with NaN
        data = data.dropna()

        if self.feature_selection:
            # Perform feature selection using CFS
            X = data.drop(self.target_column, axis=1)
            y = data[self.target_column]
            selected_features = self.select_features(X, y)
            data = pd.concat([X[selected_features], y], axis=1)

        return data

    def split_data(self, data, test_size=0.2, random_state=42):
        # Split data into training and testing sets
        X = data.drop(self.target_column, axis=1)
        y = data[self.target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        return X_train, X_test, y_train, y_test

    def select_features(self, X, y):
        # Feature selection using CFS
        selected_features = cfs.cfs(X, y)
        return X.columns[selected_features]

