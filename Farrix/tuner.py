from sklearn.model_selection import GridSearchCV

class HyperparameterTuner:
    def __init__(self, model, param_grid):
        self.model = model
        self.param_grid = param_grid

    def tune_hyperparameters(self, X_train, y_train, cv=5):
        grid_search = GridSearchCV(self.model, self.param_grid, cv=cv)
        grid_search.fit(X_train, y_train)
        return grid_search.best_estimator_