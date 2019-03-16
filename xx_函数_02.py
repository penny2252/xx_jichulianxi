# 2. 编写“学⽣管理系统”，要求如下：
# 必须使⽤⾃定义函数，完成对程序的模块化
# 学⽣信息⾄少包含：姓名、年龄、学号，除此以外可以适当添加
# 必须完成的功能：添加、删除、修改、查询、退出


student_list=[]

def print_list():
    print('\n')
    print('*' * 50)
    if student_list==[]:
        print('没有名片信息，请选择添加名片')
    else:
        print('系统中有%d 名学生信息'%(len(student_list)))
        print('-' * 30)
        print('序号\t姓名\t年龄\t学号')
        for i in range(len(student_list)):
            print('%d\t%s\t%s\t%s'%(i+1,student_list[i][0],student_list[i][1],student_list[i][2]))

def add():
    print('\n')
    print('*' * 50)
    print('添加名片')
    print('1.添加名片\n2.返回\n5.退出系统')
    print('*' * 50)
    action = input('请输入操作:1.添加名片2.返回5.退出系统')
    if action == '1':
        print('请输入信息')
        name=input('请输入姓名:')
        age_num=input('请输入年龄：')
        number=input('请输入学号：')
    elif action=='2':
        hello()
    elif action == '5':
        print('再见')
    else:
        raise Exception('输入错误，请重新输入')
    student=[name,age_num,number]
    student_list.append(student)
    hello()

def delet():
    print('\n')
    print('*' * 50)
    action = input('请输入操作：1.选择删除名片序号2返回5.退出系统')
    if action == '1':
        edit_num = int(input('请输入想要删除名片的序号'))
        student_list.pop(edit_num-1)
        print('修改完成')
        hello()
    elif action == '2':
        hello()
    elif action == '5':
        print('再见')
    else:
        raise Exception('输入错误，请重新输入')


def edit():
    print('\n')
    print('*' * 50)
    action = input('请输入操作：1.选择修改名片序号2返回5.退出系统')
    if action == '1':
        edit_num=int(input('请输入想要修改名片的序号'))
        student_list[edit_num-1][0]=input('请输入姓名：')
        student_list[edit_num-1][1]=input('请输入年龄：')
        student_list[edit_num-1][2]=input('请输入学号：')
        print('修改完成')
        hello()
    elif action == '2':
        hello()
    elif action == '5':
        print('再见')
    else:
        raise Exception('输入错误，请重新输入')



def show():
    print_list()
    print('*' * 50)
    action = input('请输入操作：1.添加名片2.删除名片3.修改名片5.退出系统')
    if action == '1':
        add()
    elif action == '2':
        delet()
    elif action == '3':
        edit()
    elif action == '5':
        print('再见')
    else:
        raise Exception('输入错误，请重新输入')


def hello():
    print('*'*50)
    print('欢迎使用名片管理系统')
    print('1.添加名片\n2.删除名片\n3.修改名片\n4.查询名片\n5.退出系统')
    print('*' * 50)
    action = input('请输入操作：1.添加名片2.删除名片3.修改名片4.查询名片5.退出系统')
    if action == '1':
        add()
    elif action == '2':
        delet()
    elif action == '3':
        edit()
    elif action == '4':
        show()
    elif action == '5':
        print('再见')
    else:
        raise Exception('输入错误，请重新输入')



try:
    hello()
except Exception as result:
    print(result)
    hello()
