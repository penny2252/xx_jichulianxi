# 1. 编程实现 9*9乘法表 提示：使⽤循环嵌套
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (j, i, i * j), end=' ')
    print('\n')
# 2.⽤函数实现求100-200⾥⾯所有的素数 提示：素数的特征是除了1和其本身能被整除，其它数都不能被整除的数
d_list = [1]
result = True


def d(num, d_list, result):
    n = 0
    for i in d_list:
        if num % i == 0:
            n += 1
    if n != 1:
        result = False
    return result


for i in range(2, 201):
    if d(i, d_list, result) != False:
        d_list.append(i)
for i in range(len(d_list)):
    if d_list[0] < 100:
        d_list.remove(d_list[0])
    else:
        break
print(d_list)


# 请⽤函数实现⼀个判断⽤户输⼊的年份是否是闰年的程序
# 提示：
# 1.能被400整除的年份
# 2.能被4整除，但是不能被100整除的年份
# 以上2种⽅法满⾜⼀种即为闰年

def term1(n):
    result = False
    if n % 400 == 0:
        result = True
    return result


def term2(n):
    result = False
    if n % 4 == 0 and n % 100 != 0:
        result = True
    return result


date = int(input('请输入年份'))

if term1(date) or term2(date) is True:
    print('%d年是闰年' % date)
else:
    print('%d年不是闰年' % date)

# ⽤函数实现输⼊某年某⽉某⽇，判断这⼀天是这⼀年的第⼏天？闰年情况也考虑进去


average_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leap(y):
    def term1(y):
        result = False
        if y % 400 == 0:
            result = True
        return result

    def term2(y):
        result = False
        if y % 4 == 0 and y % 100 != 0:
            result = True
        return result

    if term1(y) or term2(y) is True:
        return True


def day(m, d):
    days = 0
    if m == 1:
        days = d
    else:
        if leap(years) == True:
            for i in range(m - 1):
                days += leap_year[i]
            days += d
        else:
            for i in range(m - 1):
                days += average_year[i]
            days += d
    return days


date = input('请输入日期')
years = int(date[0:4])
months = int(date[4:6])
days = int(date[6:8])
print('%s是这一年的第%d' % (date, day(months, days)))

# 2. 编写“学⽣管理系统”，要求如下：
# 必须使⽤⾃定义函数，完成对程序的模块化
# 学⽣信息⾄少包含：姓名、年龄、学号，除此以外可以适当添加
# 必须完成的功能：添加、删除、修改、查询、退出
