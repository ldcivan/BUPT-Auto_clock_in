# BUPT-Auto_clock_in
北京邮电大学自动化防疫打卡
<h1>每日打卡已取消，故本项目将停止维护</h1>
<h3>部署与使用</h3>
<h5>准备</h5>
1.确认已经安装了firefox<br>
2.下载对应版本的<a href="https://github.com/mozilla/geckodriver/releases">geckodriver</a>，并将其添加到计算机环境路径中<br>
3.双击ready.bat，依照提示查验依赖等是否部署好；若有错误，请按提示核查
<h5>运行</h5>
1.在config.txt中设置你的学号与密码，并决定在运行时是否后台运行(hide=1为使用，0为不使用；同时，后台运行功能可能有bug，因为未在我的电脑上测试过)以及是否在打卡后发送邮件(email=1为使用，0为不使用；若您使用则需要在mailto后一对一设定每个账号要发送打卡报告的邮箱；邮件服务由我的服务器提供，使用发送邮件的功能则默认您接受我们记录您的目标邮箱)<br>
2.双击run.bat(有窗口版)或hide_run.bat(无窗口版)，每天0：02分时会自动打卡；若不使用后台运行，届时可能会自动弹出Firefox浏览器，这是正常的，不必惊慌。注意，初次使用时建议使用run.bat，以便在出错时及时干预。
<h5>进阶</h5>
若您还想调整打卡时间，请更改auto_sign.py中的time_interval的值(请保证Interval()中的两个时间点间隔时间为1分钟)
<h3>声明</h3>
本程序仅供学习使用，不得使用其作伪造打卡记录用。作者不会承担使用该程序带来的一切后果。
