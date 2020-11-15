import json
from backend.request import *

import time


def my_seat(cookie, is_print=True):
    if is_print:
        print("请稍候...")
    url = "http://office.chaoxing.com/data/apps/seat/index?mappId=0"

    response = get_req(url, cookie)
    seats = json.loads(response.text)["data"]["curReserves"]

    res = []
    print("+{}+{}+{}+{}+{}+{}+{}+".format("-" * 4, "-" * 13, "-" * 27, "-" * 6, "-" * 8, "-" * 21, "-" * 21))
    print("|{:^4}|{:^13}|{:^27}|{:^6}|{:^8}|{:^21}|{:^21}|".format("no", "id", "floor", "seat", "status", "startTime", "endTime"))
    print("+{}+{}+{}+{}+{}+{}+{}+".format("-" * 4, "-" * 13, "-" * 27, "-" * 6, "-" * 8, "-" * 21, "-" * 21))
    for i, one_seat in enumerate(seats):
        res.append({
            "id": str(one_seat["id"]),
            "roomId": str(one_seat["roomId"]),
            "seatNum": one_seat["seatNum"],
            "status": str(one_seat["status"])
        })

        if is_print:
            print("|{:^4}|{:^13}|{:^20}|{:^6}|{:^8}|{:^21}|{:^21}|".format(str(i), str(one_seat["id"]), one_seat["firstLevelName"] + one_seat["secondLevelName"] + one_seat["thirdLevelName"], one_seat["seatNum"], str(one_seat["status"]), convert_time(one_seat["startTime"]/1000), convert_time(one_seat["endTime"]/1000)))

    print("+{}+{}+{}+{}+{}+{}+{}+".format("-" * 5, "-" * 13, "-" * 31, "-" * 7, "-" * 7, "-" * 21, "-" * 21))
    return res


def convert_time(timestamp):
    time_local = time.localtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", time_local)
