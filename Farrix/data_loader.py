import pandas as pd
from sklearn.model_selection import train_test_split

class DataLoader:
    def __init__(self, data_source):
        self.data_source = data_source

    def load_data(self):
        # Load data from CSV file
        data = pd.read_csv(self.data_source)
        return data

    def preprocess_data(self, data):
        # Handle missing values by dropping rows with NaN
        data = data.dropna()
        return data

    def split_data(self, data, test_size=0.2, random_state=42):
        # Split data into training and testing sets
        X = data.drop('target', axis=1)
        y = data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        return X_train, X_test, y_train, y_test