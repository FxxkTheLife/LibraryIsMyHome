import json
import datetime

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
    print("------------填写必要信息----------------------")
    date = judge_input("需要预定的日期（格式为 '2020-01-01' 或直接输入向后推的天数，如明天为 1，后天为 2，退出请输 * 号）：", judge_date)
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
    print("--------------------------------------------")
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
            print("+{}+{}+{}+{}+{}+".format("-" * 9, "-" * 9, "-" * 9, "-" * 21, "-" * 21))
            print("|{:^9}|{:^9}|{:^9}|{:^21}|{:^21}|".format("Choose", "roomId", "seatNum", "startTime", "endTime"))
            print("+{}+{}+{}+{}+{}+".format("-" * 9, "-" * 9, "-" * 9, "-" * 21, "-" * 21))
            i = 0
            for i, one in enumerate(preset):
                print("|{:^9}|{:^9}|{:^9}|{:^21}|{:^21}|".format(str(i + 1), one["roomId"], one["seatNum"], one["startTime"], one["endTime"]))
            print("+{}+{}+{}+{}+{}+".format("-" * 9, "-" * 9, "-" * 9, "-" * 21, "-" * 21))
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


def input_supervise_message():
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
    print("--------------------------------------------")
    roomId = judge_input("请输入要监督的楼层（根据上述表中输入房间代号，退出请输 * 号）：", judge_floor)
    seatNum = judge_input("请输入要监督的座位（输入三位数如 '005'，退出请输 * 号）：", judge_seat)
    return roomId, seatNum


def choose_time_slice():
    choose = input("输入序号（可以选单个，也可以写0-4这种形式，不能超过4小时！！输入*退出程序），选择时段：")
    if choose == "*":
        raise KeyboardInterrupt
    choose_num=[]#存储最终选了的哪些序号
    if choose.isdigit():
        num = int(choose)
        if num < 0 or num >14:
            print("时间序号越界")
            return
        choose_num.append()
    else :
        chooses=choose.split("-")
        
        for str_num in chooses:
            if not str_num.isdigit():
                print("输入序号不正确")
                return
            choose_num.append(int(str_num))
        print(choose_num)

        for num in choose_num:
            if num < 0 or num >14:
                print("时间序号越界")
                return
        if len(choose_num)!=2:
            print("输入不正确")
            return
        return choose_num

def input_one_seat_info():
    with open("./preset/time-slice.json") as file:
        time_slices = json.load(file)
    print("------------填写必要信息----------------------")
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
    print("--------------------------------------------")
    for one_slice in time_slices:
        print(one_slice)
    print("--------------------------------------------")
    print("先设定座位，再选择时段")
    floorId = judge_input("楼层（根据上述表中输入房间代号，退出请输 * 号）：", judge_floor)
    seatId = judge_input("座位（输入三位数如 '005'，退出请输 * 号）：", judge_seat)
    
    print("+{}+{}+{}+{}+".format("-" * 9, "-" * 9, "-" * 9, "-" * 10))   
    print("|{} {} {} {}|".format("    0    " , "  7:00  ", "   ---   ", "   8:00    "))   
    print("|{} {} {} {}|".format("    1    " , "  8:00  ", "   ---   ", "   9:00    "))
    print("|{} {} {} {}|".format("    2    " , "  9:00  ", "   ---   ", "   10:00   "))
    print("|{} {} {} {}|".format("    3    " , "  10:00  ", "  ---   ", "   11:00   "))
    print("|{} {} {} {}|".format("    4    " , "  11:00  ", "  ---   ", "   12:00   "))
    print("|{} {} {} {}|".format("    5    " , "  12:00  ", "  ---   ", "   13:00   "))
    print("|{} {} {} {}|".format("    6    " , "  13:00  ", "  ---   ", "   14:00   "))
    print("|{} {} {} {}|".format("    7    " , "  14:00  ", "  ---   ", "   15:00   "))
    print("|{} {} {} {}|".format("    8    " , "  15:00  ", "  ---   ", "   16:00   "))
    print("|{} {} {} {}|".format("    9    " , "  16:00  ", "  ---   ", "   17:00   "))
    print("|{} {} {} {}|".format("    10    " , " 17:00  ", "  ---   ", "   18:00   "))
    print("|{} {} {} {}|".format("    11    " , " 18:00  ", "  ---   ", "   19:00   "))
    print("|{} {} {} {}|".format("    12    " , " 19:00  ", "  ---   ", "   20:00   "))
    print("|{} {} {} {}|".format("    13    " , " 20:00  ", "  ---   ", "   21:00   "))
    print("|{} {} {} {}|".format("    14    " , " 21:00  ", "  ---   ", "   22:00   "))
    print("+{}+{}+{}+{}+".format("-" * 9, "-" * 9, "-" * 9, "-" * 10))

    choose_nums= choose_time_slice()
    while choose_nums is None:
        choose_nums= choose_time_slice()
    startTimes = ["7:00","8:00","9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00"]
    endTimes = ["8:00","9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00"]
    i=choose_nums[0]
    while i <= choose_nums[1]:
        new_preset = {
        "roomId": floorId,
        "seatNum": seatId,
        "startTime": startTimes[i],
        "endTime": endTimes[i]
        }
        time_slices.append(new_preset)
        with open("./preset/time-slice.json", "w") as file:
            json.dump(time_slices, file)
        i+=1

def input_booking_shortcut_mess():
    with open("./preset/time-slice.json") as file:
        time_slices = json.load(file)
    date = (datetime.date.today() + datetime.timedelta(int('1'))).strftime("%Y-%m-%d")#第二天
    #date = (datetime.date.today()).strftime("%Y-%m-%d") #第一天
    slices =[]
    for chosen_slice in time_slices:
        floorId = chosen_slice["roomId"]
        seatId = chosen_slice["seatNum"]
        startTime = chosen_slice["startTime"]
        endTime = chosen_slice["endTime"]
        
        one_time_slice = []
        one_time_slice.append(date)
        one_time_slice.append(floorId)
        one_time_slice.append(seatId)
        one_time_slice.append(startTime)
        one_time_slice.append(endTime)

        slices.append(one_time_slice)
        #print(chosen_slice)
    print("----------Get:" + date + "-------------------")
    return slices


