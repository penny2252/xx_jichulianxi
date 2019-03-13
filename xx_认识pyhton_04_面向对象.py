# 编写程序，从键盘获取⽤户名和密码，然后判断，
# 如果正确就输出以下信息
# 亲爱的xxx，欢迎登陆 爱学习管理系统

class Name(object):
    pw = {'xiaoxiao': '13982121', 'pan': '883618'}
    name='a'
    psd='1'
    psd_result=False
    name_result=False
    def __init__(self):
        self.name=name=input('请输入名字')
        self.psd=psd=input('请输入qq号')
    def names(self):
        if self.name not in self.pw.keys():
            print('用户未注册请重新输入')
            self.name_result = False
        else:
            self.name_result=True
    def psds(self):
        n=self.pw[self.name]
        if self.psd not in self.pw.values():
            print('qq错误请重新输入')
            self.psd_result = False
        else:
            self.psd_result =True
    def result(self):
        Name.names(self)
        Name.psds(self)
        while not (self.name_result and self.psd_result):
            Name.__init__(self)
            Name.names(self)
            Name.psds(self)
        else:
            print('亲爱的%s，欢迎登陆 爱学习管理系统' % self.name)



name=Name()
Name.result(name)
