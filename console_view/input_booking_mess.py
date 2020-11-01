import json
from prettytable import PrettyTable


def judge_date(date):
    if date.isdecimal():
        if int(date) >= 0:
            return True
        else:
            return False
    date_str = date.split('-')
    if len(date_str) != 3:
        return False
    if len(date_str[0]) > 4 or len(date_str[1]) > 2 or len(date_str[2]) > 2:
        return False
    return True


def judge_floor(floor):
    floorNum = ["970", "971", "973", "974", "975", "976", "977", "978",
                "979", "980", "981", "982", "972", "1868", "1869", "1867",
                "1866", "1870", "1846", "1865", "1864"]
    if len(floor) > 4:
        return False
    if floor not in floorNum:
        print("楼层输入不正确。")
        return False
    if not floor.isdigit():
        print("楼层号码格式错误")
    return True


def judge_seat(seat):
    if len(seat) != 3:
        print("座位号应该为3位数字")
        return False
    if int(seat) > 300 or int(seat) < 1:
        print('座位范围要适当')
        return False
    if not seat.isdigit():
        print("座位号格式错误")
        return False
    return True


def judge_bookTime(bookTime):
    time_str = bookTime.split(':')
    if len(time_str) != 2:
        return False
    if not time_str[0].isdigit() or not time_str[1].isdigit():
        print("时间格式错误")
        return False
    # if int(str[0]) > 22 or int(str[0]) < 8 or int(str[1]) > 60 or int(str[1]) < 0:
    #     print("时间不能超出范围~")
    #     return False
    if len(time_str[1]) != 2:
        return False
    return True


def judge_positive_integer(string):
    try:
        int_value = int(string)
    except ValueError:
        return False
    if int_value <= 0:
        return False
    return True


# main fun of input
def input_booking_mess():
    with open("./preset/seat.json") as file:
        seat_preset = json.load(file)
    print("--------------------------------------------")
    print("1东  970     1西  971\n"
          "2东  973     2西  974     2内  972     2外  1868\n"
          "3内  975     3外  1869\n"
          "4内  976     4外  1867\n"
          "5内  977     5外  1866\n"
          "6内  1870    6外  978\n"
          "7内  1846\n"
          "8特  979     8老  980     8外  1865\n"
          "9内  981     9考  982     9外  1864")
    print("------------填写必要信息----------------------")
    date = judge_input("需要预定的日期（格式为 '2020-01-01' 或直接输入向后推的天数，如明天为 1，后天为 2，退出请输 * 号）：", judge_date)
    chosen_idx = choose_seat_preset(seat_preset)
    if chosen_idx is None:
        floorId = judge_input("楼层（根据上述表中输入房间代号，退出请输 * 号）：", judge_floor)
        seatId = judge_input("座位（输入三位数如 '005'，退出请输 * 号）：", judge_seat)
        startTime = judge_input("开始时间（退出请输 * 号）：", judge_bookTime)
        endTime = judge_input("结束时间（退出请输 * 号）：", judge_bookTime)
        input_str = input("是否保存座位预设？否[N/n] 是[任意键]")
        if input_str != "N" and input_str != "n":
            new_preset = {
                "roomId": floorId,
                "seatNum": seatId,
                "startTime": startTime,
                "endTime": endTime
            }
            seat_preset.append(new_preset)
            with open("./preset/seat.json", "w") as file:
                json.dump(seat_preset, file)
    else:
        chosen_seat = seat_preset[chosen_idx]
        floorId = chosen_seat["roomId"]
        seatId = chosen_seat["seatNum"]
        startTime = chosen_seat["startTime"]
        endTime = chosen_seat["endTime"]
    daynum = judge_input("预订天数（自动循环往后预订天数，仅一天输入 1，退出请输 * 号）：", judge_positive_integer)
    print("--------------------------------------")
    return date, floorId, seatId, startTime, endTime, daynum


def judge_input(prompt, judge_function):
    while True:
        input_str = input(prompt)
        if input_str == '*':
            print("好的，马上退出！")
            raise KeyboardInterrupt
        if judge_function(input_str):
            return input_str
        print("输入格式有误，请重新输入")


def choose_seat_preset(preset):
    if len(preset) > 0:
        while True:
            print("当前存在座位预设值：")
            table = PrettyTable(["Choose", "roomId", "seatNum", "startTime", "endTime"])
            i = 0
            for i, one in enumerate(preset):
                table.add_row([str(i + 1), one["roomId"], one["seatNum"], one["startTime"], one["endTime"]])
            print(table)
            try:
                res = int(input("是否使用座位预设值，是则输入序号，否则按 0："))
            except ValueError:
                continue
            else:
                if res == 0:
                    return None
                if 1 <= res <= i + 1:
                    return res - 1
    return None
