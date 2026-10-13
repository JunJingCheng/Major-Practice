from ucimlrepo import fetch_ucirepo, list_available_datasets
import pandas as pd
from pathlib import Path

"""
list_available_datasets()    
name                                  id
...
Breast Cancer Wisconsin (Original)    15
...
"""

__all__ = ['fetch_local_bcw']


def _fetch_bcw_df(save=False, save_path="data/Breast Cancer Wisconsin.csv"):
    bcw = fetch_ucirepo(name="Breast Cancer Wisconsin (Original)")
    bcw_df = pd.concat([bcw.data.features, bcw.data.targets], axis=1)
    bcw_df.to_csv(save_path, mode="w", index=False, encoding="utf-8") if save else ...
    return bcw_df


def fetch_local_bcw(path="./data/Breast Cancer Wisconsin.csv"):
    if type(path) not in [Path, str]:
        raise TypeError()
    path = Path(path) if type(path) is str else path
    if (path.exists()) and (path.suffix == ".csv"):
        return pd.read_csv(path)
    raise FileNotFoundError(f"Not found {path}")


def main():
    ...


if __name__ == "__main__":    
    _fetch_bcw_df(save=True)