import pickle
from pathlib import Path

import polars as pl
from sklearn.preprocessing import LabelEncoder as SkLabelEncoder

from .base_encoder import BaseEncoder


class LabelEncoder(BaseEncoder):

    def __init__(self):
        self.encoder = SkLabelEncoder()
        self.is_fitted = False
    
    def fit(self, df: pl.DataFrame, column: str) -> "LabelEncoder":
        values = df[column].to_list()
        self.encoder.fit(values)
        self.is_fitted = True
        return self
    def transfrom(self, df: pl.DataFrame, column: str)