# 1. 编程实现对⼀个元素全为数字的列表，求最⼤值、最⼩值

a = [1, 2, 3, 4, 5, 6, 7, 9, 9, 213, 123, 12321]
print(max(a))
print(min(a))
print('-' * 50)

# 2. 编写程序，完成以下要求：
# 统计字符串中，各个字符的个数
# ⽐如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1

a = 'hello world'
print(a)
# 转列表
a_list = list(a)
a_listo = []
# 删除空格
n = a.count(' ')
for i in range(n):
    a_list.remove(' ')
for i in a_list:
    if i not in a_listo:
        a_listo.append(i)
for i in a_listo:
    j = a.count(i)
    print('%s:%d  ' % (i, j), end='')
print('\n')

# 3. 编写程序，完成以下要求：
# 完成⼀个路径的组装,先提示⽤户多次输⼊路径，最后显示⼀个完成的路径，⽐如 /home/python/ftp/share
a = input('请输入路径深度')
path = ''
for i in range(int(a)):
    path += '/'
    path += input('请逐步输入路径')
print(path)
print('-' * 50)


# 编写程序，完成“名⽚管理器”项⽬需要完成的基本功能：
# 1. 添加名⽚
# 2. 删除名⽚
# 3. 修改名⽚
# 4. 查询名⽚
# 5. 退出系统
# 程序运⾏后，除⾮选择退出系统，否则重复执⾏功能


def add():
    print('2.删除名片\n3.修改名片\n4.查询名片\n5.退出系统')
    action = input('请输入操作')
    if action == '2':
        delet()
    elif action == '3':
        change()
    elif action == '4':
        show()
    elif action == '5':
        print('再见')
    else:
        raise Exception('输入错误，请重新输入')


def delet():
    print('1.添加名片\n3.修改名片\n4.查询名片\n5.退出系统')
    action = input('请输入操作')
    if action == '1':
        add()
    elif action == '3':
        change()
    elif action == '4':
        show()
    elif action == '5':
        print('再见')
    else:
        raise Exception('输入错误，请重新输入')


def change():
    print('1.添加名片\n2.删除名片\n4.查询名片\n5.退出系统')
    action = input('请输入操作')
    if action == '1':
        add()
    elif action == '2':
        delet()
    elif action == '4':
        show()
    elif action == '5':
        print('再见')
    else:
        raise Exception('输入错误，请重新输入')


def show():
    print('1.添加名片\n2.删除名片\n3.修改名片\n5.退出系统')
    action = input('请输入操作')
    if action == '1':
        add()
    elif action == '2':
        delet()
    elif action == '3':
        change()
    elif action == '5':
        print('再见')
    else:
        raise Exception('输入错误，请重新输入')


def hello():
    print('1.添加名片\n2.删除名片\n3.修改名片\n4.查询名片\n5.退出系统')
    action = input('请输入操作')
    if action == '1':
        add()
    elif action == '2':
        delet()
    elif action == '3':
        change()
    elif action == '4':
        show()
    elif action == '5':
        print('再见')
    else:
        raise Exception('输入错误，请重新输入')
        hello()


try:
    hello()
except Exception as result:
    print(result)
