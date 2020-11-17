import re

from backend.request import *


def get_seat_token(roomId, day, cookie):
    url = "http://office.chaoxing.com/front/apps/seat/select?id={}&day={}&backLevel=2".format(roomId, day)

    response = get_req(url, cookie)
    text = response.text

    res = re.search('token: \'[A-Za-z0-9]*\'', text)
    token = text[res.span()[0]: res.span()[1]].split("'")[1]
    return token


def gotcha(roomId, startTime, endTime, day, seatNum, token, cookie):
    url = "http://office.chaoxing.com/data/apps/seat/submit?roomId=" + roomId + \
          "&startTime=" + startTime + \
          "&endTime=" + endTime + \
          "&day=" + day + \
          "&seatNum=" + seatNum + \
          "&token=" + token

    return get_req(url, cookie).text
