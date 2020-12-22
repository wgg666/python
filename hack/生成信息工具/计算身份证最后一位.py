""" 
身份证每一位下标对应[7, 9, 10, 5, 8, 4, 2,1, 6, 3, 7, 9, 10, 5, 8, 4, 2]下标相乘，
列表存放每一位相乘的结果，
计算列表元素之和
%11的到下标
['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']找下标对应的元素
 """

def check_sfz_last(digs:str) -> str:
    """ 
    check_sfz_last  校验身份证最后一位
    :digs   身份证前17位
     """
    #校验码
    Check_list = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    #加权因子
    Weighting_factor = [7, 9, 10, 5, 8, 4, 2,1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # digs = input('身份证前17位: ')
    # isdigit检测字符串是否只由数字组成。
    if len(digs) != 17 or digs.isdigit() == False:
        print('incorrect input')
    else:
        return Check_list[sum([int(digs[i]) * Weighting_factor[i] for i in range(17)]) % 11]

if __name__ == "__main__":
    print(check_sfz_last('37097718131215956'))