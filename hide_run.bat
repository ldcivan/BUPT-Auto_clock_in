@echo off
chcp 65001
title 正在运行
if "%1"=="hide" goto CmdBegin
start mshta vbscript:createobject("wscript.shell").run("""%~0"" hide",0)(window.close)&&exit
:CmdBegin
python auto_sign.py
pause
