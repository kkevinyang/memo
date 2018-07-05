# coding=utf8

# import os
import subprocess
import traceback
# subprocess.Popen(PLAYER_1 + " " + file); #非阻塞
# subprocess.Popen(PLAYER_1 + " " + file).wati(); #阻塞

print('start....')

try:
	file_sys = [
		"C:\Program Files (x86)\NetSarang\Xshell 5\Xshell.exe",
		"C:\Program Files (x86)\MdCharm\MdCharm.exe",
		"C:\Program Files\JetBrains\PyCharm 2017.3\bin\pycharm64.exe",
		"C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE",
		"C:\exe\SwitchHosts\SwitchHosts.exe",
		"C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe",
		"C:\Users\yangkai\AppData\Local\youdao\dict\Application\YoudaoDict.exe",
		"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe",
		"C:\\Users\\yangkai\\AppData\\Local\\Postman\\app-5.3.2\\Postman.exe",
	]
	print(" ".join(file_sys))
	for x in file_sys:
		name = x.split('\\')[-1]
		try:
			subprocess.Popen(x)
			print(u'start {0}sucess！'.format(name))

		except:
			print(u'启动{0}失败！'.format(name))
			try:
				subprocess.call('start "" {}'.format(x), shell=True)
			except:
				print(u'启动{0}再次失败,so sad'.format(name))
	# subprocess.Popen(" ".join(file_sys))

except:
	traceback.print_exc()
	import time
	time.sleep(10)
print(u'启动命令成功，按下任意键结束脚本。。。')
a = raw_input()
