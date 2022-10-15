# BUPT-Auto_clock_in
北京邮电大学自动化防疫打卡
<h3>部署与使用</h3>
<h5>准备</h5>
1.确认已经安装了firefox<br>
2.下载对应版本的<a href="https://github.com/mozilla/geckodriver/releases">geckodriver</a>，并将其添加到计算机环境路径中<br>
3.双击ready.bat，依照提示查验依赖等是否部署好；若有错误，请按提示核查
<h5>运行</h5>
1.在config.txt中设置你的学号与密码，并决定在运行时是否后台运行(后台运行可能有bug，因为未在我的电脑上测试过)<br>
2.双击run.bat，每天0：02分时会自动打卡；届时可能会自动弹出Firefox浏览器，这是正常的，不必惊慌。
<h5>进阶</h5>
若您还想调整打卡时间，请更改auto_sign.py中的time_interval的值(请保证Interval()中的两个时间点间隔时间为1分钟)
<h3>声明</h3>
本程序仅供学习使用，不得使用其作伪造打卡记录用。作者不会承担使用该程序带来的一切后果。
