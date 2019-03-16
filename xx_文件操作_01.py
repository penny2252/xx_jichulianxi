# 任务描述
# 输入文件的名字,然后程序自动完成对文件进行备份
file_name=input('请输入要复制的文件名')
file_newlist=file_name.split('.')

file_newname=file_newlist[0]+'复制.'+file_newlist[1]

file_old=open(file_name,'r')
file_new=open(file_newname,'w')

temp=file_old.read()
file_new.write(temp)

file_old.close()
file_new.close()


#正确答案
# 提示输入文件
# oldFileName = input("请输入要拷⻉的文件名字:")
# # 以读的方式打开文件
# oldFile = open(oldFileName,'rb')
# # 提取文件的后缀
# fileFlagNum = oldFileName.rfind('.')
# if fileFlagNum > 0:
# fileFlag = oldFileName[fileFlagNum:]
# # 组织新的文件名字
# newFileName = oldFileName[:fileFlagNum] + '[复件]' + fileFlag
# # 创建新文件
# newFile = open(newFileName, 'wb')
# # 把旧文件中的数据,一行一行的进行复制到新文件中
# for lineContent in oldFile.readlines():
# newFile.write(lineContent)
# # 关闭文件
# oldFile.close()
# newFile.close()