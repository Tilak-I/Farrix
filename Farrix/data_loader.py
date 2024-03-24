import pandas as pd
from sklearn.model_selection import train_test_split

class DataLoader:
    def __init__(self, data_source, target_column):
        self.data_source = data_source
        self.target_column = target_column

    def load_data(self):
        # Load data from CSV file
        data = pd.read_csv(self.data_source)
        return data

    def preprocess_data(self, data):
        # Handle missing values by dropping rows with NaN
        data = data.dropna()
        data = data.select_dtypes(include=['float64', 'int64'])
        return data

    def split_data(self, data, test_size=0.2, random_state=42):
        # Split data into training and testing sets
        X = data.drop(self.target_column, axis=1)  # Features
        y = data[self.target_column]  # Target
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        return X_train, X_test, y_train, y_test