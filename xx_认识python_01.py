# 1、编写程序，完成以下要求：
# 提示⽤户进⾏输⼊数据
# 获取⽤户的数据数据（需要获取2个）
# 对获取的两个数字进⾏求和运⾏，并输出相应的结果

# 判断输入


def num_type(num):
    num_typ = None
    while True:
        try:
            int(num)
            num_typ = '整数'
            return num_typ
        except:
            try:
                float(num)
                num_typ = '小数'
                return num_typ
            except:
                try:
                    complex(num)
                    num_typ = '复数'
                    return num_typ
                except ValueError:
                    return num_typ


def digatl(num):
    fuzhi_n = None
    if num_type(num) == '整数':
        fuzhi_n = int(num)
    elif num_type(num) == '小数':
        fuzhi_n = float(num)
    elif num_type(num) == '复数':
        fuzhi_n = complex(num)
    return fuzhi_n


def shuru():
    num = input('请输入一个数字')
    while num_type(num) is None:
        num = input('输入的不是整数、小数或者复数格式，请重新输入一个数字')
    return num


num1 = shuru()
num2 = shuru()
print('您输入的数值是:%s(%s);%s(%s)' % (digatl(num1), num_type(num1), digatl(num2), num_type(num2)))
print('两个数值相加的结果是:%s' % str(digatl(num1) - digatl(num2)))
