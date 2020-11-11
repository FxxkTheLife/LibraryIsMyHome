from backend.request import *


def sign(reserveId, cookie):
    url = "http://office.chaoxing.com/data/apps/seat/sign?id=" + str(reserveId)

    response = get_req(url, cookie)

    return response.text


def sign_back(reserveId, cookie):
    url = "http://office.chaoxing.com/data/apps/seat/signback?id=" + str(reserveId)

    response = get_req(url, cookie)

    return response.text
