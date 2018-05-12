# _*_ coding=utf-8 _*_

import os

# 1:表示添加标签，2:表示删除标签
print('*'*40)
print('  1、添加标签           2、删除标签')
print('*'*40)
funflag = input('请输入您的选择：')

# 指定文件的路径
folderName = './RenameFile'

# 获取指定路径的所有文件的名字
dirList = os.listdir(folderName)

# 遍历输出所有文件名字
for name in dirList:
	if funflag == 1:
		newName = '[bling]-' + name
	elif funflag == 2:
		num = len('[bling]-')
		newName = name[num:]
	print(newName)

