# _*_ coding=utf-8 _*_

'''
	简单文件的备份 程序设计思路：
		1、用户可自主输入文件名(灵活)
		2、配置新文件的名字(旧文件名+‘复件’+后缀)
			1、先从右向左查找文件的后缀
			2、判断文件后缀长度是否大于0(是否存在)
			3、先截取文件名的后缀
			4、配置新文件的名字(旧文件名+‘复件’+后缀)
		3、打开新的文件
		4、将旧文件中的内容写入到新的文件中
		5、关闭新旧文件
'''

# 文件的拷贝
oldfileName = input('请输入要拷贝文件的名字(含后缀)：')

# 以只读模式打开旧文件
oldFile = open(oldfileName, 'r')

# 判断文件是否打开成功
if oldFile:
	# 此部分主要是设置新的文件名

	# 从右向左查找文件的后缀
	fileFlagNum = oldfileName.rfind('.')

	# 判断文件的后缀是否存在
	if fileFlagNum > 0:

		# 截取旧文件名的后缀	
		fileFlag = oldfileName[fileFlagNum:]

	# 配置新的文件名（旧文件名+'复件'+旧文件的后缀）
	newFileName = oldfileName[:fileFlagNum]+'复件'+fileFlag

	# 以只写模式打开新的文件
	newFile = open(newFileName, 'w')

	# 循环按行一次性读出旧文件中的内容
	for lineContent in oldFile.readlines():

		# 将旧文件中的内容写入到新的文件中
		newFile.write(lineContent)

	# 关闭旧文件
    oldFile.close()

    # 关闭新文件
    newFile.close()

print('再看看文件是否存在吧！')