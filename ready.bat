@echo off
chcp 65001
title 正在安装依赖
python  --version
if errorlevel 1 (
	echo 您未安装python或pip，快去官网下一个吧！
	pause
	goto end
)

pip --version
if errorlevel 1 (
	echo 您未安装python或pip，快去官网下一个吧！
	pause
	goto end
)

echo 确认python与pip已安装

pip install -r requirements.txt
echo 若未提示error，则依赖安装完毕

where geckodriver.exe
if errorlevel 1 (
	echo 未查找到geckodriver，请前往https://github.com/mozilla/geckodriver/releases下载对应版本！  下载解压后请务必将 getckodriver.exe 添加到 Path 环境变量中(可运行PATH.bat辅助)
	pause
	goto end
)

where firefox.exe
if errorlevel 1 (
	echo 未查找到firefox浏览器，若已安装请忽略
)
:end
pause