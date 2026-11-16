"""
The following methods are implemented by deepseek:
1. RoughSetsReducer.core, RoughSetsReducer.reduce

Seek for more details at
https://chat.deepseek.com/a/chat/s/a4e879b0-9409-4853-9a84-2267ba5e61ee 
"""



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

    def core(self):
            """
            计算决策系统的核属性 (Core)
            返回: 包含核属性名称的 list
            """
            print("正在计算核属性 (Core)...")
            core_attrs = []
            
            # 获取原始条件属性集 C 对决策属性 V 的依赖度
            gamma_c = self.gamma(self.C)
            
            # 遍历条件属性集中的每一个属性
            for a in self.C:
                # 构造去掉属性 a 之后的剩余属性集
                remain_attrs = [attr for attr in self.C if attr != a]
                
                # 计算去掉 a 之后的依赖度
                gamma_remain = self.gamma(remain_attrs)
                
                # 如果依赖度下降（严格小于），说明属性 a 是核属性
                # 注意：使用 1e-6 容差防止浮点数精度误差
                if gamma_remain < gamma_c - 1e-6:
                    core_attrs.append(a)
                    
            print(f"核属性计算完成，Core 包含: {core_attrs}")
            return core_attrs

    def reduce(self):
        """
        基于依赖度的前向启发式属性约简 (Reduction)
        返回: 约简后的属性名称 list
        """
        print("正在执行属性约简 (Reduction)...")
        
        # 1. 获取原始依赖度（目标依赖度）
        gamma_c = self.gamma(self.C)
        
        # 2. 以核属性作为起点
        red_attrs = self.core()
        current_gamma = self.gamma(red_attrs)
        
        # 3. 如果核属性的依赖度已经等于原始依赖度，直接返回
        if current_gamma >= gamma_c - 1e-6:
            print(f"核属性已满足分类能力，直接返回: {red_attrs}")
            return red_attrs
            
        # 4. 开始前向贪心搜索
        # 候选属性集：不在当前约简集里的属性
        candidates = [attr for attr in self.C if attr not in red_attrs]
        
        while current_gamma < gamma_c - 1e-6 and candidates:
            best_attr = None
            best_gamma = current_gamma
            max_delta = -1
            
            # 遍历所有候选属性，寻找能带来最大依赖度提升的属性
            for a in candidates:
                # 尝试加入属性 a
                test_attrs = red_attrs + [a]
                test_gamma = self.gamma(test_attrs)
                
                # 计算增量
                delta = test_gamma - current_gamma
                
                # 更新最优选择
                if delta > max_delta:
                    max_delta = delta
                    best_gamma = test_gamma
                    best_attr = a
            
            # 如果找到了能让依赖度提升的属性，就加入
            if best_attr is not None and max_delta > 1e-6:
                red_attrs.append(best_attr)
                current_gamma = best_gamma
                candidates.remove(best_attr)
                print(f"  [+] 加入属性: {best_attr}, 当前依赖度: {current_gamma:.4f}")
            else:
                # 如果遍历了一圈，没有任何属性能让依赖度提升，说明无法再约简了，跳出循环
                print("  [!] 没有属性可以继续提升依赖度，停止搜索。")
                break
                
        print(f"属性约简完成，Reduct 包含: {red_attrs}")
        print(f"原始依赖度: {gamma_c:.4f}, 约简后依赖度: {current_gamma:.4f}")
        return red_attrs