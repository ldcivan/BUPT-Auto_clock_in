from selenium import webdriver
from pyvirtualdisplay import Display
import time
import sys
from interval import Interval
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

def write(data):
    File = open('log.txt', mode='a', encoding="utf-8")
    File.write(data + '\n')
    File.close()

def daka(user, pw, mailto, hidden):
    global window
    print(user)
    print(pw)
    print(mailto)
    print(hidden)
    if hidden == 1:
        write("使用后台模式")
        print("您决定使用后台模式运行")
        try:
            window = Display(visible=False, size=(800, 600))
            write("正在启动虚拟窗口")
            print("正在启动虚拟窗口")
            window.start()
            write("虚拟窗口已开启")
            print("虚拟窗口已开启")
        except:
            write("不支持后台模式，已回归默认")
            print("您的电脑不支持后台模式，接下来将以前台模式运行\n无需担心，若一切正常，前台浏览器会自动关闭")
            hidden = 0

    write("正在启动浏览器")
    print("正在启动浏览器")
    driver = webdriver.Firefox()
    driver.set_window_position(x=-10000, y=-10000)
    write("浏览器已启动，正在打开目标")
    print("浏览器已启动，正在打开网页，目标app.bupt.edu.cn")
    driver.get("https://app.bupt.edu.cn/ncov/wap/default/index")

    try:
        driver.execute_script("this.vm.hasFlag = 0;this.vm.info = this.vm.oldInfo;this.vm.info.created = Number(Date.parse( new Date() ).toString().substr(0,10));var now = new Date();var year = now.getFullYear().toString();var month = now.getMonth().toString();var date = now.getDate().toString();if (month < 10) month = '0' + month;if (date < 10) date = '0' + date;this.vm.info.date = Number(year + month + date);this.vm.save();")
    except:
        write("无法自动登录，正在尝试使用学号及密码登录")
        print("无法自动登录，正在尝试使用学号及密码登录")
        try:
            time.sleep(3)
            driver.execute_script("var username ='" + user + "';var password ='" + pw + "';localStorage.loginTypeUsername = 'password';if (username && password) {parent.doLogin( username, password, 'username_password');}")
        except:
            write("在登陆页面出错，可能是账号密码错误")
            print("在登陆页面出错，可能是账号密码错误")
            driver.quit()
            if hidden == 1:
                window.stop()
            sys.exit()

        time.sleep(3)
        if driver.current_url == "https://app.bupt.edu.cn/ncov/wap/default/index":
            write("登陆成功")
            print("登陆成功")
            try:
                driver.execute_script("this.vm.hasFlag = 0;this.vm.info = this.vm.oldInfo;this.vm.info.created = Number(Date.parse( new Date() ).toString().substr(0,10));var now = new Date();var year = now.getFullYear().toString();var month = now.getMonth().toString();var date = now.getDate().toString();if (month < 10) month = '0' + month;if (date < 10) date = '0' + date;this.vm.info.date = Number(year + month + date);this.vm.save();")
                write(user + "打卡成功")
                print(user + "打卡成功，如果是首次使用，建议人工查看是否已打卡")
            except:
                write(user + "打卡失败")
                print(user + "打卡失败，请手动打卡")
        else:
            write("登陆失败，可能是浏览器未正确跳转")
            print("登陆失败，可能是浏览器未正确跳转")

    time.sleep(2)

    if hidden == 1:
        window.stop()
        write("虚拟窗口已关闭")
        print("虚拟窗口已关闭")
    driver.quit()
    write("浏览器已关闭")
    print("浏览器已关闭")

    if mailto != 0:
        with open('./log.txt', encoding='utf-8') as file:
            content = file.read()
        content = content.split("#")[-1]
        data = {'mailto': mailto, 'subject': '防疫打卡报告', 'body': content}
        #  data = dict(mailto=mailto, subject='防疫打卡报告', body=content)
        r = requests.post("http://pro-ivan.com/comment/email_pub.php", data=data, headers=headers)
        print(r.text)


with open("./geckodriver.log", 'w') as file:
    file.truncate(0)
with open("./log.txt", 'w') as file:
    file.truncate(0)
print("log初始化成功")
write("读取config")
print("正在读取config.txt")
with open('./config.txt', 'r') as file:
    l = file.readlines()  # 按行读取TXT文件，都是字符串类型
    d = {}
    for i in l:
        s = i.replace('\n', '')  # 去除换行符
        s0 = s.split(sep=':')  # 以:分割字符串，左边是键，右边是值。同样都是字符串类型
        if '"' in s0[1]:
            s0[1] = s0[1].replace('"', '')  # 字符串存在双引号，说明原本的值就是字符串类型。去掉多余的双引号
        else:
            s0[1] = int(s0[1])  # 说明原本值是整型，强制类型转换
        d[s0[0]] = s0[1]  # 键值对添加到字典中


user = d['username']
user = user.split(",")
pw = d['pw']
pw = pw.split(",")
mailto = d['mailto']
mailto = mailto.split(",")
hidden = d['hidden']
email = d['email']

while True:
    # 当前时间
    now_localtime = time.strftime("%H:%M:%S", time.localtime())
    # 当前时间（以时间区间的方式表示）
    now_time = Interval(now_localtime, now_localtime)

    time_interval = Interval("00:00:00", "23:02:00")

    if now_time in time_interval:
        with open("./log.txt", 'w') as file:
            file.truncate(0)
        write("#" + str(now_time) + "开始打卡")
        print("#开始打卡")

        def indexing(lst, index):
            if lst[index:] == []:
                print("IndexError: list index out of range")

        for i in range(len(user)):
            try:
                indexing(pw, i)
                indexing(mailto, i)
                if email == 1:
                    daka(user[i], pw[i], mailto[i], hidden)
                if email == 0:
                    daka(user[i], pw[i], 0, hidden)
            except:
                print("出现错误，可能是因为密码/邮箱数组越界")
                write("出现错误，可能是因为密码/邮箱数组越界")
        time.sleep(120)
    else:
        write(str(now_time) + "  等待")
        print("等待")
        time.sleep(40)
