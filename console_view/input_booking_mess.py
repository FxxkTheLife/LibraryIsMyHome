import re
import prettytable


def judge_date(date):
    str = date.split('-')
    if len(str) != 3:
        return False
    if len(str[0]) > 4 or len(str[1]) > 2 or len(str[2]) > 2:
        return False
    print(str)
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
    str = bookTime.split(':')
    if len(str) != 2:
        return False
    if not str[0].isdigit() or not str[1].isdigit():
        print("时间格式错误")
        return False
    # if int(str[0]) > 22 or int(str[0]) < 8 or int(str[1]) > 60 or int(str[1]) < 0:
    #     print("时间不能超出范围~")
    #     return False
    if len(str[1]) != 2:
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
    date = judge_input("需要预定的日期(2020-00-00的格式)：", judge_date)
    floorId = judge_input("楼层：", judge_floor)
    seatId = judge_input("座位：", judge_seat)
    startTime = judge_input("开始时间：", judge_bookTime)
    endTime = judge_input("结束时间：", judge_bookTime)
    daynum = judge_input("预订天数（自动循环往后预订天数，仅一天输入 1）：", judge_positive_integer)
    print("--------------------------------------")
    return date, floorId, seatId, startTime, endTime, daynum


def judge_input(prompt, judge_function):
    while True:
        input_str = input(prompt)
        if input_str == '*':
            print("好的,马上退出！")
            raise KeyboardInterrupt
        if judge_function(input_str):
            return input_str
        print("输入格式有误，请重新输入(输入星号'*'退出)")
