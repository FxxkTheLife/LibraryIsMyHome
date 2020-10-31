from my_seat import my_seat
from start import start_login, start_reserve
from sign import sign, sign_back

from console_view.input_booking_mess import input_booking_mess
from console_view.console_login import console_login

import json
from prettytable import PrettyTable


def console_home():
    with open("./console_view/preset.json") as file:
        preset = json.load(file)
    uname, password, idx = console_login(preset)
    cookie, name = start_login(uname, password)
    print("已登录！")

    if idx is None:
        input_str = input("是否保存帐号密码？否[N/n] 是[任意键]")
        if input_str != "N" and input_str != "n":
            new_preset = {
                "uname": uname,
                "password": password,
                "name": name
            }
            preset["login"].append(new_preset)
    else:
        preset["login"][idx]["name"] = name
    with open("./console_view/preset.json", "w") as file:
        json.dump(preset, file)

    while True:
        table = PrettyTable(["Choose", "Operation"])
        table.add_row(["0", "退出"])
        table.add_row(["1", "查询已订"])
        table.add_row(["2", "签到"])
        table.add_row(["3", "签退"])
        table.add_row(["4", "订座"])

        print(table)
        num = input("选择：")
        if not num.isdigit():
            continue
        if int(num) > 4 or int(num) < 0:
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


def show_seats(cookie):
    my_seat(cookie)
    input("回车继续")


def sign_seat(cookie):
    seats = my_seat(cookie)

    while True:
        choose = input("选择签到座位：")
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
        choose = input("选择退签座位（批量退订请加英文逗号 '1, 2, 3' 或使用短横线符号 '3-9'，可混合使用）：")
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
    for i in range(0, int(daynum)):
        print("正在预订第 " + str(i+1) + "/" + daynum + " 天")
        start_reserve(roomId, startTime, endTime, date, seatNum, cookie)
        split = date.split("-")
        day = int(split[2]) + 1
        date = split[0] + "-" + split[1] + "-" + str(day)
