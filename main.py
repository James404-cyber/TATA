import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("module")
elif 'aarch' in arc:
	__import__("module64")
else:
	exit(f' Unknow device machine {arc}')
