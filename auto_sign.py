from selenium import webdriver
from pyvirtualdisplay import Display
import time
import sys
from interval import Interval

def daka():
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
    pw = d['pw']
    hidden = d['hidden']

    global window

    if hidden == 1:
        print("您决定使用后台模式运行")
        try:
            window = Display(visible=False, size=(800, 600))
            print("正在启动虚拟窗口")
            window.start()
            print("虚拟窗口已开启")
        except:
            print("您的电脑不支持后台模式，接下来将以前台模式运行\n无需担心，若一切正常，前台浏览器会自动关闭")
            hidden = 0

    print("正在启动浏览器")
    driver = webdriver.Firefox()
    driver.set_window_position(x=-10000, y=-10000)
    print("浏览器已启动正在打开网页，目标app.bupt.edu.cn")
    driver.get("https://app.bupt.edu.cn/ncov/wap/default/index")

    try:
        driver.execute_script("this.vm.hasFlag = 0;this.vm.info = this.vm.oldInfo;this.vm.info.created = Number(Date.parse( new Date() ).toString().substr(0,10));var now = new Date();var year = now.getFullYear().toString();var month = now.getMonth().toString();var date = now.getDate().toString();if (month < 10) month = '0' + month;if (date < 10) date = '0' + date;this.vm.info.date = Number(year + month + date);this.vm.save();")
    except:
        print("无法自动登录，正在尝试使用学号及密码登录")
        try:
            time.sleep(3)
            driver.execute_script("var username ='" + user + "';var password ='" + pw + "';localStorage.loginTypeUsername = 'password';if (username && password) {parent.doLogin( username, password, 'username_password');}")
        except:
            print("在登陆页面出错，可能是账号密码错误")
            driver.quit()
            if hidden == 1:
                window.stop()
            sys.exit()

        time.sleep(3)
        if driver.current_url == "https://app.bupt.edu.cn/ncov/wap/default/index":
            print("登陆成功")
            try:
                driver.execute_script("this.vm.hasFlag = 0;this.vm.info = this.vm.oldInfo;this.vm.info.created = Number(Date.parse( new Date() ).toString().substr(0,10));var now = new Date();var year = now.getFullYear().toString();var month = now.getMonth().toString();var date = now.getDate().toString();if (month < 10) month = '0' + month;if (date < 10) date = '0' + date;this.vm.info.date = Number(year + month + date);this.vm.save();")
                print("打卡成功，如果是首次使用，建议人工查看是否已打卡")
            except:
                print("打卡失败，请手动打卡")
        else:
            print("登陆失败，可能是浏览器未正确跳转")

    time.sleep(2)

    if hidden == 1:
        window.stop()
        print("虚拟窗口已关闭")
    driver.quit()
    print("浏览器已关闭")


while True:
    # 当前时间
    now_localtime = time.strftime("%H:%M:%S", time.localtime())
    # 当前时间（以时间区间的方式表示）
    now_time = Interval(now_localtime, now_localtime)

    time_interval = Interval("00:02:00", "00:03:00")

    if now_time in time_interval:
        print("开始打卡")
        daka()
        time.sleep(120)
    else:
        print("等待")
        time.sleep(40)
