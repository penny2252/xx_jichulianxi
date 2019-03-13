# 编写程序，从键盘获取⼀个⼈的信息，然后按照下
# ⾯格式显示
# ==================================
# 姓名: dongGe
# QQ:xxxxxxx
# ⼿机号:131xxxxxx
# 公司地址:北京市xxxx
# ==================================

name = input('请输入姓名')
qq_num = input('请输入qq')
tel_num = input('请输入电话')
add = input('请输入地址')

print('=' * 34)
print('姓名：%s' % name)
print('QQ：%s' % qq_num)
print('电话：%s' % tel_num)
print('地址：%s' % add)
print('=' * 34)
