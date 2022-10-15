@echo off
chcp 65001
title 添加PATH指导
sysdm.cpl
echo 现在请确认弹出了一个窗口，我们的操作将由此开始
pause
echo 接下来，点开【高级】，他在最上面的那一行中
pause
echo 接下来，点开【环境变量】，他在窗口靠下的位置
pause
echo 接下来，新的窗口会弹出；小心，现在的操作很重要；如果没有经验，请跟着我慢慢来
pause
echo 找到【系统变量】，他在窗口的下半部分
pause
echo 找到【变量】一行下的【PATH】
pause
echo 双击他，请确认现在又弹出了一个窗口
pause
echo 使用滑条将页面拉到最下方，你会看到一行空行，双击他
pause
echo 现在，在里面输入你的 geckodriver.exe 的路径，其状如【D:\Program Files\geckodriver-v0.31.0-win64】
pause
echo 通过【确认】关闭之前打开的所有窗口
pause
echo 之后请重新运行 ready.bat，如无额外报错，则安装成功
pause