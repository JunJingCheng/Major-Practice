from ucimlrepo import fetch_ucirepo, list_available_datasets
import pandas as pd
from pathlib import Path, WindowsPath

"""
list_available_datasets()    
name                                  id
...
Breast Cancer Wisconsin (Original)    15
...
"""

__all__ = ['fetch_local_bcw']

DATA_DIR = Path("data")
ORIGINAL_BCW_PATH = DATA_DIR / "Breast Cancer Wisconsin.csv"


def _fetch_bcw_online(save=False, save_path=ORIGINAL_BCW_PATH):
    bcw = fetch_ucirepo(name="Breast Cancer Wisconsin (Original)")
    bcw_df = pd.concat([bcw.data.features, bcw.data.targets], axis=1)
    bcw_df.to_csv(save_path, mode="w", index=False, encoding="utf-8") if save else ...
    return bcw_df


def fetch_local_bcw(path="data/Clear Breast Cancer Wisconsin.csv"):
    if type(path) not in [Path, str, WindowsPath]:
        raise TypeError()
    path = Path(path) if type(path) is str else path
    if (path.exists()) and (path.suffix == ".csv"):
        return pd.read_csv(path)
    raise FileNotFoundError(f"Not found {path}")


if __name__ == "__main__":   
    # list_available_datasets()
    _fetch_bcw_online(save=True)