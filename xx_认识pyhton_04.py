# 编写程序，从键盘获取⽤户名和密码，然后判断，
# 如果正确就输出以下信息
# 亲爱的xxx，欢迎登陆 爱学习管理系统


def inputqq(name):
    # pw_name = input('请输入qq号')
    # if pw_name == pw[name]:
    #     print('亲爱的%s，欢迎登陆 爱学习管理系统' % name)
    # else:
    #     for i in range (4):
    #         if pw_name==pw[name]:
    #             print('亲爱的%s，欢迎登陆 爱学习管理系统' % name)
    #             break
    #         print('qq错误，请重新输入')
    #         pw_name = input('请输入qq号')
    #
    #     print('qq错误次数超过5次，请重新输入姓名')
    #     inputname()
    pw_name = input('请输入qq号')
    n=1
    while pw_name != pw[name]:

        print('qq错误，请重新输入')
        pw_name = input('请输入qq号')
        n += 1
        if n == 5:
            print('qq错误次数超过5次，请重新输入姓名')
            inputname()

    print('亲爱的%s，欢迎登陆 爱学习管理系统' % name)
    # break

def inputname():
    name = input('请输入姓名:')
    if name not in pw.keys():
        print('尚未注册，请重新输入')
        inputname()
    else:

        inputqq(name)



pw = {'xiaoxiao':'13982121','pan':'883618'}

name=inputname()
