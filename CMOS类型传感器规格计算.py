def cmos():

    print("现在请输入传感器输出照片长边的最大像素值")
    pixel_max = int(input())
    print("现在请输入传感器尺寸的分子（分数形式）")
    size_up = float(input())
    print("现在请输入传感器尺寸的分母（分数形式）")
    size_down = float(input())
    size = size_up/size_down
    print("请输入传感器长边所占比例")
    len_long = float(input())
    print("请输入传感器短边所占比例")
    len_short = float(input())
    real_len_long = len_long*(((size**2)/(len_long**2+len_short**2))**0.5)*16
    real_len_short = len_short*(((size**2)/(len_long**2+len_short**2))**0.5)*16
    real_size = real_len_long*real_len_short
    cut_k = (1872**0.5)/(16*size)
    pixel_size = (real_len_long/pixel_max)*1000
    print("传感器的实际长度为",real_len_long,"毫米")
    print("传感器的实际宽度为",real_len_short,"毫米")
    print("传感器的实际面积为",real_size,"平方毫米")
    print("传感器的裁切系数为",cut_k)
    print("传感器的单位像素尺寸（即单位像素的边长）为",pixel_size,"微米\n")

while True:
    cmos()
