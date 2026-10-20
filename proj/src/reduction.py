import pandas as pd
# from src.preprocessing import fetch_clear_bcw


def equiv_cls(B):
    equiv_cls_B = dict()
    for r in U.groupby(B, group_keys=True).apply(lambda x: x).index:
        if r[0:-1] not in equiv_cls_B.keys():
            equiv_cls_B[r[0:-1]] = [r[-1]]
            continue
        equiv_cls_B[r[0:-1]].append(r[-1])
    return {k: set(equiv_cls_B[k]) for k in equiv_cls_B.keys()}


def under_appr(B, X):
    under_appr_ind_set = set()
    X_ind_set = set(X.index)
    for cls_set in equiv_cls(B).values():
        if not cls_set.issubset(X_ind_set): continue
        under_appr_ind_set = under_appr_ind_set.union(cls_set)
    return X.loc[list(under_appr_ind_set)]


def pos(B):
    _U_div_D = {tuple(d): U[(U[V]==d).all(axis=1)] for d in D}
    under_appr_dict = {k: under_appr(B, D_i) for k, D_i in _U_div_D.items()}
    return pd.concat(under_appr_dict.values())


def gamma(B): return len(pos(B)) / len(U)


if __name__ == "__main__":
    ...
