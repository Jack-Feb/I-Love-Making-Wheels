# 检查缺失的数据
def check_missing_data(df):
    return df.isnull().sum().sort_values(ascending=False)

# 分类变量转换为数值变量
def convert_cat2num(df):
    num_encode = {'col_1' : {'YES':1, 'NO':0},
                  'col_2'  : {'WON':1, 'LOSE':0, 'DRAW':0}}  
    df.replace(num_encode, inplace=True)
   
# 将最后三个字符为aaa的字符串拼接
def concat_col_str_condition(df):
    mask = df['col_1'].str.endswith('aaa', na=False)
    col_new = df[mask]['col_1'] + df[mask]['col_2']
    col_new.replace('aaa', ' ', regex=True, inplace=True) 
    
def drop_multiple_col(cl_names_list,df): 
    df.drop(col_names_list, axis=1, inplace=True)
    return df
