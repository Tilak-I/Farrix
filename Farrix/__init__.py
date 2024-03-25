from .data_loader import DataLoader
from .model import Model
from .linear_regression import LinearRegression
from .decision_tree_classifier import DecisionTreeClassifier
from .evaluation_metrics import EvaluationMetrics
from .visualization import Visualization
from .tuner import HyperparameterTuner
from .utils import Utils

import pandas as pd
# Allows users to designate imports and allows for 'from Farrix import *' to import everything


class DataSet(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

__all__ = [
    'DataLoader',
    'Model',
    'LinearRegression',
    'DecisionTreeClassifier',
    'EvaluationMetrics',
    'Visualization',
    'HyperparameterTuner',
    'Utils'
]
