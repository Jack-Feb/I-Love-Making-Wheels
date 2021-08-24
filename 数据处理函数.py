# 检查缺失的数据
def check_missing_data(df):
    return df.isnull().sum().sort_values(ascending=False)

def convert_cat2num(df):
