from Farrix import DataLoader, LinearRegression, EvaluationMetrics, Visualization

# Load data
data_loader = DataLoader('stock_data.csv', 'Close')
data = data_loader.load_data()
data = data_loader.preprocess_data(data)

# Split data
X_train, X_test, y_train, y_test = data_loader.split_data(data)

# Train linear regression model
model = LinearRegression()
model.train(X_train, y_train)
# Visualize data
visualizer = Visualization()
visualizer.plot_data(data.drop('Close', axis=1), data['Close'])

# Evaluate model
metrics = EvaluationMetrics()
mse = metrics.mse(y_test, model.predict(X_test))
print(f'Mean Squared Error: {mse}')

r2 = metrics.r2(y_test, model.predict(X_test))
print(f'R-squared: {r2}')

#visualizer.plot_model_performance(model, X_test, y_test) - Throws an error (fix later)
