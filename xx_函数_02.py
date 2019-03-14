# 2. 编写“学⽣管理系统”，要求如下：
# 必须使⽤⾃定义函数，完成对程序的模块化
# 学⽣信息⾄少包含：姓名、年龄、学号，除此以外可以适当添加
# 必须完成的功能：添加、删除、修改、查询、退出

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
