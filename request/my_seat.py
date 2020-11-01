import json
from request.request import *

from prettytable import PrettyTable
import time


def my_seat(cookie):
    print("请稍候...")
    url = "https://office.chaoxing.com/data/apps/seat/index?mappId=0"

    response = get_req(url, cookie)
    seats = json.loads(response.text)["data"]["curReserves"]

    res = []
    table = PrettyTable(["no", "id", "floor", "seat", "status", "startTime", "endTime"])
    for i, one_seat in enumerate(seats):
        res.append({
            "id": str(one_seat["id"]),
            "roomId": str(one_seat["roomId"]),
            "seatNum": one_seat["seatNum"]
        })

        table.add_row([str(i), str(one_seat["id"]), one_seat["firstLevelName"] + one_seat["secondLevelName"] + one_seat["thirdLevelName"], one_seat["seatNum"], str(one_seat["status"]), convert_time(one_seat["startTime"]/1000), convert_time(one_seat["endTime"]/1000)])
    print(table)
    return res


def convert_time(timestamp):
    time_local = time.localtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", time_local)
