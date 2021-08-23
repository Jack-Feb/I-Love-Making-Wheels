def findprime(a):
    list_ = []
    _list = []
    while a>1:
        for i in range(2,a+1):
            if a % i == 0:
                a = int(a/i)
                if a == 1:
                    list_.append(i)
                else:
                    _list.append(i)
                break     
    list_all = list_ + _list
    # print(list_all)
