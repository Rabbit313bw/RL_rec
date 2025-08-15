import abc
from pathlib import Path
from typing import Any
import polars as pl


class BaseEncoder(abc.ABC):
    
    @classmethod
    def fit(self, df: pl.DataFrame, column: str) -> "BaseEncoder":
        pass

    @classmethod
    def transform(self, df: pl.DataFrame, column: str, output_column: str) -> pl.DataFrame:
        pass 

    def fit_transform(self, df: pl.DataFrame, column: str, output_column: str) -> pl.DataFrame:
        self.fit(df, column)
        return self.transform(df, column, output_column)
    
    @classmethod
    def save(self, path: Path) -> None:
        pass

    @classmethod
    def load(self, path: Path) -> "BaseEncoder":
        pass
