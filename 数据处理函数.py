def check_missing_data(df):
    # 检查缺失的数据
    return df.isnull().sum().sort_values(ascending=False)
