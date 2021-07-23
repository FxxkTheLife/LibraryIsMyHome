import re

from backend.request import *


def get_seat_token(roomId, day, cookie):
    url_page = "http://office.chaoxing.com/front/apps/seat/list?deptIdEnc="
    page_res = get_req(url_page, cookie)  # request 'url_page' to get the pageToken, it's in the page_res.text

    page_token_match = re.search('&pageToken=\' \+ \'[A-Za-z0-9]*\'', page_res.text)  # find it's index
    page_token = page_res.text[page_token_match.span()[0]: page_token_match.span()[1]].split("'")[2]  

    url = "http://office.chaoxing.com/front/apps/seat/select?id={}&day={}&backLevel=2&pageToken={}".format(roomId, day, page_token)

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
