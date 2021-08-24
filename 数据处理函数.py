# 检查缺失的数据
def check_missing_data(df):
    return df.isnull().sum().sort_values(ascending=False)

# 分类变量转换为数值变量
def convert_cat2num(df):
    num_encode = {'col_1' : {'YES':1, 'NO':0},
                  'col_2'  : {'WON':1, 'LOSE':0, 'DRAW':0}}  
    df.replace(num_encode, inplace=True)
