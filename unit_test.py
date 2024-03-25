from Farrix import DataLoader, LinearRegression, EvaluationMetrics, Visualization
import Farrix

# Load data
data_loader = DataLoader('housing_data.csv', 'price')
data = data_loader.load_data()
data = data_loader.preprocess_data(data)

# Visualize data
visualizer = Visualization()
visualizer.plot_data(data.drop('price', axis=1), data['price'])

# Split data
X_train, X_test, y_train, y_test = data_loader.split_data(data)

# Train linear regression model
model = LinearRegression()
model.train(X_train, y_train)

# Evaluate model
metrics = EvaluationMetrics()
mse = metrics.mse(y_test, model.predict(X_test))
r2 = metrics.r2(y_test, model.predict(X_test))
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Visualize model performance
visualizer.plot_model_performance(model, X_test, y_test)

# Predict the price of a new house
new_house = Farrix.DataSet({'size': [2100], 'bedrooms': [4], 'bathrooms': [3], 'location': ['urban']})
predicted_price = model.predict(new_house)
print(f'Predicted price for the new house: ${predicted_price[0]:.2f}')