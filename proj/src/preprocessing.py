import pandas as pd
from utils.fetch_bcw_dataset import fetch_local_bcw, DATA_DIR, ORIGINAL_BCW_PATH
from pathlib import Path

NONA_BCW_PATH = DATA_DIR / "NoNA Breast Cancer Wisconsin.csv"
CLEAR_BCW_PATH = DATA_DIR / "Clear Breast Cancer Wisconsin.csv"


def del_na_row(original=None, save=False, save_path=NONA_BCW_PATH):
    bcw_df = fetch_local_bcw(ORIGINAL_BCW_PATH) if original is None else original
    nona_bcw_df = bcw_df[~bcw_df['Bare_nuclei'].isna()]
    nona_bcw_df.to_csv(save_path, mode="w", index=False, encoding="utf-8") if save else ...
    return nona_bcw_df


def fetch_nona_bcw(path=NONA_BCW_PATH):
    return fetch_local_bcw(path=path)


def foolish_discretization(original: pd.Series, category_num: int=5):
    original_max = original.max()
    original_min = original.min()
    pos_series = original - original_min
    unit_diff = pos_series.max() / category_num
    discretized = pos_series // unit_diff
    return discretized


def entropy_discretization(): raise NotImplementedError()


def kmean_discretization(): raise NotImplementedError()


discretization = foolish_discretization


def clear_bcw_df(nona_bcw_df=None, save=False, save_path=CLEAR_BCW_PATH):
    nona_bcw_df = fetch_nona_bcw() if nona_bcw_df is None else nona_bcw_df 
    clear_bcw_df = nona_bcw_df.copy()
    clear_bcw_df['Bare_nuclei'] = discretization(nona_bcw_df['Bare_nuclei']).astype("int64")
    clear_bcw_df.to_csv(save_path, mode="w", index=False, encoding="utf-8") if save else ...
    return clear_bcw_df


def fetch_clear_bcw(path=CLEAR_BCW_PATH):
    return fetch_local_bcw(path=path)


if __name__ == "__main__":
    del_na_row(save=True)
    clear_bcw_df(save=True)