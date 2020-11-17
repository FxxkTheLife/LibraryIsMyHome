from backend.reserve import *
import json


def supervise(roomId, seatNum, cookie):
    url = "http://office.chaoxing.com/data/apps/seat/reserve/info?id={}&seatNum={}".format(roomId, seatNum)

    response = get_req(url, cookie)

    try:
        responseJson = json.loads(response.text)
        reserveId = responseJson["data"]["seatReserve"]["id"]
    except KeyError:
        print("监督失败，现在无人使用")
        return response.text

    url = "http://office.chaoxing.com/data/apps/seat/supervise?id=" + str(reserveId)

    response = get_req(url, cookie)
    print("当前此座位的预约 id 是：" + str(reserveId))
    return response.text
