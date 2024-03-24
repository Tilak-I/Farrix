# __init__.py

from .data_loader import DataLoader
from .model import Model
from .linear_regression import LinearRegression
from .decision_tree_classifier import DecisionTreeClassifier
from .evaluation_metrics import EvaluationMetrics
from .visualization import Visualization
from .tuner import HyperparameterTuner
from .utils import Utils

#Allows users to designate imports and allows for 'from Farrix import *' to import everything

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