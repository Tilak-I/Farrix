from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

class Utils:
    def handle_missing_values(self, data):
        imputer = SimpleImputer(strategy='mean')
        imputed_data = imputer.fit_transform(data)
        return imputed_data

    def feature_scaling(self, data):
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data)
        return scaled_data