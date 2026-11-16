import pandas as pd
import numpy as np

def extract_rules(df_reduced, target_col='Class', min_support=0.01, min_confidence=0.8):
    """
    从约简后的决策表中提取决策规则
    
    参数:
        df_reduced: 约简后的 DataFrame（包含约简特征和 target_col）
        target_col: 决策属性列名
        min_support: 最小支持度阈值
        min_confidence: 最小置信度阈值
    返回:
        包含规则的 DataFrame
    """
    # 1. 统计总的样本数
    total_samples = len(df_reduced)
    
    # 2. 提取条件属性列
    feature_cols = [col for col in df_reduced.columns if col != target_col]
    
    # 3. 按照所有条件属性进行分组，统计每个等价类中目标类的频数
    # groupby 的 size() 可以得到满足当前条件组合的样本总数
    grouped = df_reduced.groupby(feature_cols + [target_col]).size().reset_index(name='count')
    
    rules = []
    
    # 4. 遍历分组结果，计算支持度和置信度
    for _, row in grouped.iterrows():
        # 当前等价类（前件）匹配的样本数
        count_X_and_d = row['count']
        
        # 构建条件前件 (X)
        antecedents = []
        for col in feature_cols:
            # 将列名和值组合，例如 "Clump_thickness = 5"
            antecedents.append(f"{col} = {row[col]}")
        antecedent_str = " AND ".join(antecedents)
        
        # 获取后件 (d)
        consequent = f"{target_col} = {row[target_col]}"
        
        # 计算支持度 (满足前件且后件发生的样本 / 总样本数)
        support = count_X_and_d / total_samples
        
        # 计算满足当前前件（无论后件是什么）的样本总数
        # 可以通过再次筛选原表得到，或者更高效的方法是：
        mask = (df_reduced[feature_cols] == row[feature_cols]).all(axis=1)
        count_X = df_reduced[mask].shape[0]
        
        # 计算置信度 (满足前件且后件发生的样本 / 满足前件的样本)
        confidence = count_X_and_d / count_X
        
        # 5. 根据阈值过滤规则
        if support >= min_support and confidence >= min_confidence:
            rules.append({
                'Antecedent (IF)': antecedent_str,
                'Consequent (THEN)': consequent,
                'Support': round(support, 4),
                'Confidence': round(confidence, 4),
                'Coverage': count_X_and_d
            })
            
    # 转换为 DataFrame 并按置信度降序排列
    rules_df = pd.DataFrame(rules)
    if not rules_df.empty:
        rules_df = rules_df.sort_values(by=['Confidence', 'Support'], ascending=[False, False]).reset_index(drop=True)
        
    return rules_df