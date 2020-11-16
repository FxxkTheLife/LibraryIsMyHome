from backend.my_seat import my_seat
from backend.start import start_login, start_reserve
from backend.sign import sign, sign_back
from backend.supervise import supervise
from backend.exception import *

from console_view.input_booking_mess import input_booking_mess, input_supervise_message
from console_view.console_login import console_login

import json
import datetime
import time
import random


def console_home():
    print("\033[33m===========================================\033[0m")
    print("\033[33m----------👋欢迎使用订座专用脚本～～-----------\033[0m")

    with open("./preset/login.json") as file:
        preset = json.load(file)

    while True:
        try:
            uname, password, idx = console_login(preset)
            cookie, name = start_login(uname, password)
        except LoginException as e:
            print("发生错误：{}".format(e.message))
        else:
            break

    print("已登录！")

    if idx is None:
        input_str = input("是否保存帐号密码？否[N/n] 是[任意键]")
        if input_str != "N" and input_str != "n":
            new_preset = {
                "uname": uname,
                "password": password,
                "name": name
            }
            preset.append(new_preset)
    else:
        preset[idx]["name"] = name
    with open("./preset/login.json", "w") as file:
        json.dump(preset, file)

    while True:
        print("+{}+{}+".format("-"*11, "-"*14))
        print("|{:^11}|{:^14}|".format("Choose", "Operation"))
        print("+{}+{}+".format("-"*11, "-"*14))
        print("|{:^11}|{:^13}|".format("0", "退出"))
        print("|{:^11}|{:^11}|".format("1", "查询已订"))
        print("|{:^11}|{:^13}|".format("2", "签到"))
        print("|{:^11}|{:^13}|".format("3", "退座"))
        print("|{:^11}|{:^13}|".format("4", "订座"))
        print("|{:^11}|{:^13}|".format("5", "监督"))
        print("|{:^11}|{:^12}|".format("6", "反监督"))
        print("+{}+{}+".format("-"*11, "-"*14))

        num = input("选择：")
        if not num.isdigit():
            continue

        num = int(num)
        if num == 0:
            raise KeyboardInterrupt
        elif num == 1:
            show_seats(cookie)
        elif num == 2:
            sign_seat(cookie)
        elif num == 3:
            cancel_seat(cookie)
        elif num == 4:
            book_seat(cookie)
        elif num == 5:
            supervise_seat(cookie)
        elif num == 6:
            anti_supervise(cookie)


def show_seats(cookie):
    my_seat(cookie)
    input("回车继续")


def sign_seat(cookie):
    seats = my_seat(cookie)

    while True:
        choose = input("选择签到座位（退出请输 * 号）：")
        if choose == '*':
            return  # 回到主界面
        if choose.isdigit():
            choose = int(choose)
            if choose >= len(seats) or choose < 0:
                print("序号出错")
                continue
        else:
            print("输入错误")
            continue
        break
    print(sign(seats[choose]["id"], cookie))
    input("回车继续")


def cancel_seat(cookie):
    seats = my_seat(cookie)

    while True:
        choose = input("选择退座座位（批量退订请加英文逗号分隔间断的序号 '1, 2, 3' 或使用短横线符号连接连续的序号 '3-9'，可混合使用，退出请输 * 号）：")
        if choose == '*':
            return  # 回到主界面
        if choose.isdigit():
            choose = int(choose)
            if choose >= len(seats) or choose < 0:
                print("序号出错")
                continue
            print(sign_back(seats[choose]["id"], cookie))
        else:
            chooses = choose.split(",")
            continue_flag = False
            try:
                for choose in chooses:
                    one_choose = choose.split("-")
                    if len(one_choose) == 1:
                        idx = int(one_choose[0])
                        if idx >= len(seats) or idx < 0:
                            print("序号出错")
                            continue_flag = True
                            break
                        print(sign_back(seats[int(one_choose[0])]["id"], cookie))
                    elif len(one_choose) == 2:
                        start = int(one_choose[0])
                        end = int(one_choose[1])
                        if start < 0 or end >= len(seats) or end - start < 0:
                            print("序号出错")
                            continue_flag = True
                            break
                        for one_sign in range(start, end+1):
                            print(sign_back(seats[one_sign]["id"], cookie))
                    else:
                        raise ValueError
            except ValueError:
                print("输入错误")
                continue
            if continue_flag:
                continue
        break

    input("回车继续")


def book_seat(cookie):
    try:
        date, roomId, seatNum, startTime, endTime, daynum = input_booking_mess()
    except KeyboardInterrupt:
        return
    if date.isdecimal():
        date = (datetime.date.today() + datetime.timedelta(int(date))).strftime("%Y-%m-%d")
    for i in range(0, int(daynum)):
        print("正在预订第 " + str(i+1) + "/" + daynum + " 天")
        start_reserve(roomId, startTime, endTime, date, seatNum, cookie)
        split = date.split("-")
        date = datetime.date(int(split[0]), int(split[1]), int(split[2])) + datetime.timedelta(1)
        date = date.strftime("%Y-%m-%d")


def supervise_seat(cookie):
    try:
        roomId, seatNum = input_supervise_message()
    except KeyboardInterrupt:
        return

    print(supervise(roomId, seatNum, cookie))
    input("回车继续")


def anti_supervise(cookie):
    i = 1
    delay_seconds = 240

    try:
        input("回车开始运行反监督程序，此程序需一直在后台运行，每隔 " + str(delay_seconds) + " 秒检测一次，[Ctrl-C] 结束")
        print("反监督中...")
        while True:
            res = my_seat(cookie, is_print=False)
            print("反监督中..." + "，你当前订了 " + str(len(res)) + " 个位置")
            for one_res in res:
                if one_res["status"] == "5":
                    print("检测到监督，正在签到...")
                    print(sign(one_res["id"], cookie))
                    print("完成")
            delay_seconds = random.randint(180, 280)
            print("已检测完第 " + str(i) + " 次啦，我要休息 " + str(delay_seconds) + " 秒")
            time.sleep(delay_seconds)
            i += 1
    except KeyboardInterrupt:
        return
