from selenium import webdriver
from pyvirtualdisplay import Display
import time
from interval import Interval
import requests
import tkinter as tk
import tkinter.messagebox as msgbox
import sys
import os.path

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

def default_config():
    new_config = open("./config_default.txt", 'w', encoding="utf-8")
    new_config.write(
        'username:"XXXXXXXX,XXXXXXXX"\npw:"12345678,12345678"\nmailto:"XXXXXXXXX@qq.com"\nhidden:1\nemail:1\nfirefox_path:""')
    new_config.close()

def write(data):
    File = open('log.txt', mode='a', encoding="utf-8")
    File.write(data + '\n')
    File.close()

def daka(user, pw, mailto, hidden, executable_path):
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
    try:
        driver = webdriver.Firefox(executable_path=executable_path)
    except:
        msgbox.showerror("浏览器驱动错误", "可能是geckodriver.exe未添加到PATH，或者程序未查找到FireFox路径\n若是后种情况，请在config.txt中将firefox.exe的完整路径填入firefox_path:")
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
            msgbox.showerror("登陆失败", user + "登陆失败，可能是账号或密码错误，请检查您的帐号与密码是否正确且一一对应")
            #  win32api.MessageBox(0, user + "登陆失败，可能是账号或密码错误，请检查您的帐号与密码是否正确且一一对应", "登陆失败", win32con.MB_ICONWARNING)
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
                windows = tk.Tk()
                msgbox.showerror("打卡失败", user + "打卡失败，请手动打卡")
                #  win32api.MessageBox(0, user + "打卡失败，请手动打卡", "打卡失败", win32con.MB_ICONWARNING)
                write(user + "打卡失败")
                print(user + "打卡失败，请手动打卡")
                windows.destroy()
        else:
            msgbox.showerror("登录失败", user + "登录失败，可能是浏览器未正确跳转，请重试或在GitHub反馈")
            #  win32api.MessageBox(0, user + "登录失败，可能是浏览器未正确跳转，请重试或在GitHub反馈", "登陆失败", win32con.MB_ICONWARNING)
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

    if mailto != 0:  #  递送打卡报告
        with open('./log.txt', encoding='utf-8') as file:
            content = file.read()
        content = content.split("#")[-1]
        data = {'mailto': mailto, 'subject': '防疫打卡报告', 'body': content}
        #  data = dict(mailto=mailto, subject='防疫打卡报告', body=content)
        r = requests.post("http://pro-ivan.com/comment/email_pub.php", data=data, headers=headers)
        print(r.text)



root0 = tk.Tk()
msgbox.showinfo("BUPT自动防疫打卡","程序已开始运行，具体运行日志请参考log.txt")
root0.destroy()
#  判断是否展示条约
if not os.path.isfile("./readed"):
    root1 = tk.Tk()
    #  rule = win32api.MessageBox(0, "使用本程序带来的后果，YujioNako与Pro-Ivan概不负责，如不同意该条件请勿使用本程序！", "声明", win32con.MB_YESNO)
    rule = msgbox.askyesno("声明", "使用本程序带来的后果，YujioNako与Pro-Ivan概不负责，如不同意该条件请勿使用本程序！\n是否同意该规则？")
    if rule == 0:
        sys.exit()
    elif rule == 1:
        file = open("./readed", 'w', encoding="utf-8")
        file.write("本文档的存在意味着您接受我们的条约，即使用本程序带来的后果，YujioNako与Pro-Ivan概不负责。敬请知悉。")
        file.close()
    root1.destroy()


with open("./geckodriver.log", 'w') as file:
    file.truncate(0)
with open("./log.txt", 'w') as file:
    file.truncate(0)
print("log初始化成功")
write("读取config")
print("正在读取config.txt")

if not os.path.isfile("./config.txt"):  #  config初始设置GUI
    #  print("初次使用吗？是的话请告诉我们您的BUPT账号和密码吧！")
    root2 = tk.Tk()
    first_time = msgbox.askyesno("欢迎使用", "欢迎使用由YujioNako编写的BUPT自动打卡程序！您似乎是第一次使用本程序，需要钰中帮您配置账密吗？或者您也可以选“否”，然后根据我们提供的config_default.txt自行配置后将文件名改为config.txt")
    if first_time == 0:
        default_config()
        sys.exit()
    #  user = input("账号：")
    #  pw = input("密码：")
    root = tk.Tk()
    root.title("请输入您的学号与密码")
    root.geometry('300x240')

    def input2config():
        user = b0.get()
        pw = b1.get()
        new_config = open("./config.txt", 'w', encoding="utf-8")
        new_config.write('username:"' + user + '"\npw:"' + pw + '"\nmailto:""\nhidden:1\nemail:0\nfirefox_path:""')
        new_config.close()
        msgbox.showinfo("config已设置", "基本设置录入成功！更多设置请自行查看config.txt")
        print("基本设置录入成功！更多设置请自行查看config.txt")
        root.destroy()
        try:
            root2.destroy()
        except:
            return

    b3 = tk.Label(root, text="学号：")
    b3.pack()
    b0 = tk.Entry(root, text='学号', width=20)
    b0.pack()
    b4 = tk.Label(root, text="密码：")
    b4.pack()
    b1 = tk.Entry(root, text='密码', width=20)
    b1.pack()
    b2 = tk.Button(root, text='确 认', command=input2config)
    b2.pack()
    b5 = tk.Label(root, text="注：您可以英文“,”分隔以输入多组账密")
    b5.pack()
    root.mainloop()

try:
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
    executable_path = d['firefox_path']
    print("完成config的读取")
    write("完成config的读取")
except:
    msgbox.showerror("config异常", "可能是config.txt内格式错误，请从目录内找到config_default.txt进行参考")
    #  win32api.MessageBox(0, "可能是config.txt内格式错误，请从目录内找到config_default.txt进行参考", "config异常", win32con.MB_ICONWARNING)
    default_config()
    write("config异常")
    print("config异常")
    sys.exit()


while True:
    # 当前时间
    now_localtime = time.strftime("%H:%M:%S", time.localtime())
    # 当前时间（以时间区间的方式表示）
    now_time = Interval(now_localtime, now_localtime)

    time_interval = Interval("00:02:00", "00:03:00")

    if now_time in time_interval:
        with open("./log.txt", 'w') as file:
            file.truncate(0)
        write("#" + str(now_time) + "开始打卡")
        print("#开始打卡")

        def indexing(lst, index):
            if lst[index:] == []:
                msgbox.showwarning("IndexError", "list index out of range")
                #  win32api.MessageBox(0, "list index out of range", "IndexError", win32con.MB_ICONWARNING)
                print("IndexError: list index out of range")

        for i in range(len(user)):
            try:
                indexing(pw, i)
                indexing(mailto, i)
                if email == 1:
                    daka(user[i], pw[i], mailto[i], hidden, executable_path)
                if email == 0:
                    daka(user[i], pw[i], 0, hidden, executable_path)
            except:
                msgbox.showerror("错误", "可能是因为config.txt内密码/邮箱数组越界，请检查config.txt")
                #  win32api.MessageBox(0, "可能是因为config.txt内密码/邮箱数组越界，请检查config.txt", "错误", win32con.MB_ICONWARNING)
                print("出现错误，可能是因为密码/邮箱数组越界")
                write("出现错误，可能是因为密码/邮箱数组越界")
                sys.exit()
        time.sleep(120)
    else:
        write(str(now_time) + "  等待")
        print("等待")
        time.sleep(40)
