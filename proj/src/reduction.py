import pandas as pd
from src.preprocessing import fetch_clear_bcw


class RoughSetsReducer:

    def __init__(self, U=None):
        self.U = fetch_clear_bcw() if U is None else U
        self.C = list(self.U.columns[0:-1])
        self.V = [c for c in self.U.columns if c not in self.C]
        self.D = self.U[self.V].drop_duplicates().to_numpy()

    def equiv_cls(self, B):
        equiv_cls_B = dict()
        for r in self.U.groupby(B, group_keys=True).apply(lambda x: x).index:
            if r[0:-1] not in equiv_cls_B.keys():
                equiv_cls_B[r[0:-1]] = [r[-1]]
                continue
            equiv_cls_B[r[0:-1]].append(r[-1])
        return {k: set(equiv_cls_B[k]) for k in equiv_cls_B.keys()}

    def under_appr(self, B, X):
        under_appr_ind_set = set()
        X_ind_set = set(X.index)
        for cls_set in self.equiv_cls(B).values():
            if not cls_set.issubset(X_ind_set): continue
            under_appr_ind_set = under_appr_ind_set.union(cls_set)
        return X.loc[list(under_appr_ind_set)]

    def pos(self, B):
        _U_div_D = {tuple(d): self.U[(self.U[self.V]==d).all(axis=1)] for d in self.D}
        under_appr_dict = {k: self.under_appr(B, D_i) for k, D_i in _U_div_D.items()}
        return pd.concat(under_appr_dict.values())

    def gamma(self, B): return len(self.pos(B)) / len(self.U)

    def core(self): raise NotImplementedError()

    def reduce(self): raise NotImplementedError()
