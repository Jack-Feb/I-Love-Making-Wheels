# 检查缺失的数据
def check_missing_data(df):
    return df.isnull().sum().sort_values(ascending=False)

# 分类变量转换为数值变量
def convert_cat2num(df):
    num_encode = {'col_1' : {'YES':1, 'NO':0},
                  'col_2'  : {'WON':1, 'LOSE':0, 'DRAW':0}}  
    df.replace(num_encode, inplace=True)
    
def concat_col_str_condition(df):
    # concat 2 columns with strings if the last 3 letters of the first column are 'pil'
    mask = df['col_1'].str.endswith('pil', na=False)
    col_new = df[mask]['col_1'] + df[mask]['col_2']
    col_new.replace('pil', ' ', regex=True, inplace=True)  # replace the 'pil' with emtpy space

