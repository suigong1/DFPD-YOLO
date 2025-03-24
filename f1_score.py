def calculate_f1_score_from_pr(precision, recall):
    # 检查是否精确率和召回率都为0，避免除以0的情况
    if (precision + recall) == 0:
        return 0
    # 计算F1分数
    f1_score = 2 * (precision * recall) / (precision + recall)
    return f1_score

# 示例
p = 0.909  # 精确率
r = 0.813 # 召回率

f1 = calculate_f1_score_from_pr(p, r)
print(f"F1 Score: {f1:.4f}")
