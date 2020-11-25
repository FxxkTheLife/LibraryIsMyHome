import json
import datetime
from input_booking_mess import *

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
    



def book_seat_shortcut():
    with open("./preset/time-slice.json") as file:
        time_slices = json.load(file)
    date = (datetime.date.today() + datetime.timedelta(int('1'))).strftime("%Y-%m-%d")#第二天
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
        print(chosen_slice)
    print("----------Get:" + date + "-------------------")
    print(chosen_slice)
    return slices


sl=book_seat_shortcut()
