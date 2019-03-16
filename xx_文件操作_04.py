#实现文件存储功能
import os

student_file='xx_名片.txt'

def read():
    if student_file in os.listdir():
        file = open(student_file, 'r')
        student = file.readlines()
        file.close()

    else:
        file = open(student_file, 'w')
        file.close()
        student=[]
    return student

def write(student):
    file=open(student_file,'w')
    for i in student:
        file.write(i)
    file.close()


def print_list():
    print('\n')
    print('*' * 50)
    student=read()
    if student==[]:
        print('没有名片信息，请选择添加名片')
    else:
        print('系统中有%d 名学生信息'%(len(student)))
        print('-' * 30)
        print('序号\t姓名\t年龄\t学号')
        for i in range(len(student)):
            print('%d\t%s'%(i+1,student[i]))


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
    student_new=name+' '*10+age_num+' '*10+number+'\n'
    student=read()
    student+=student_new
    write(student)

    hello()

def delet():
    print('\n')
    print('*' * 50)
    action = input('请输入操作：1.删除名片2返回5.退出系统')
    if action == '1':
        student=read()
        edit_num = int(input('请输入想要删除名片的序号'))
        student.pop(edit_num-1)
        write(student)
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
    action = input('请输入操作：1.修改名片2返回5.退出系统')
    if action == '1':
        edit_num=int(input('请输入想要修改名片的序号'))
        name=input('请输入姓名：')
        age_num=input('请输入年龄：')
        number=input('请输入学号：')
        student_new = name + ' ' * 10 + age_num + ' ' * 10 + number + '\n'
        student=read()
        student[edit_num-1]=student_new
        write(student)
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
