# 1. 读取一个文件,显示除了以井号(#)开头的行以外的所有行
file=open('xx_文件操作_01.py','r')
temp=file.readlines()

for i in temp:
    if i[0]!='#':
        print(i)
