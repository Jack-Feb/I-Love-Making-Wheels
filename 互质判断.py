# this is a test file.

choose = 1
def choose_not_re():     # 用户控制台封装一下，函数名起长是为了防止与内建函数重名
    global choose
    datas = str(input('输入0退出，否则继续运行'))
    if datas == '0':
        choose = 0
    else:
        choose = 1

while choose == 1:  
    p = int(input('请输入整数p  '))
    q = int(input('请输入整数q  '))
    p_min = 2         # 公因数1无意义
    q_min = 2
    list_p = [i for i in range(p_min,p+1)]     # 生成从2到p（range左闭右开，故加一）的自然数列表
    list_q = [i for i in range(q_min,q+1)]
    list_p_end = []
    list_q_end = []
    for p_ in list_p:
        if p%p_ == 0:       #暴力试错
            list_p_end.append(p_)
    for q_ in list_q:
        if q%q_ == 0:
            list_q_end.append(q_)

    list_all = list_p_end + list_q_end
    list_len = len(list_all)
    list_len_only = len(set(list_all))     # 依靠减少重复操作后两列表元素数量之和是否变化判断是否有公因数

    if list_len > list_len_only:
        list_re = [x for x in list_p_end if x in list_q_end]      # 仅在合适情况下进行查重操作，减少资源开支
        print('p与q的公因数有：')
        print(list_re)
        choose_not_re()
    else:
        print('p与q互质')
        choose_not_re()

        
def cmos ():        # 这个函数是原来的版本，变量不易阅读，留此存档
    print("现在请输入传感器输出照片长边的最大像素值")
    i=int(input())
    print("现在请输入传感器尺寸的分子（分数形式）")
    z=float(input())
    print("现在请输入传感器尺寸的分母（分数形式）")
    y=float(input())
    a=z/y
    print("2")
    b=float(input())
    print("请输入传感器短边所占比例")
    c=float(input())
    d=b*(((a**2)/(b**2+c**2))**0.5)*16
    e=c*(((a**2)/(b**2+c**2))**0.5)*16
    f=d*e
    g=(1872**0.5)/(16*a)
    h=(d/i)*1000
    print("传感器的实际长度为",d,"毫米")
    print("传感器的实际宽度为",e,"毫米")
    print("传感器的实际面积为",f,"平方毫米")
    print("传感器的裁切系数为",g)
    print("传感器的单位像素尺寸（即单位像素的边长）为",h,"微米")
