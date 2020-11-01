from request.login import *
from request.reserve import *
import json


def start_login(uname, password):
    cookie = ""

    # login
    print("1")
    cookie_str, text = login(uname, password)
    cookie = merge_cookie(cookie, cookie_str)
    print("Cookie: ", cookie)
    print("Res text: ", text)

    # text to json object
    text_json = json.loads(text)

    # login get more cookie
    print("2")
    url = text_json["url"].replace("https", "http")
    cookie_str, text = get_req_to_cookie(url, cookie_str)
    cookie = merge_cookie(cookie, cookie_str)
    print("Cookie: ", cookie)
    print("Res text: ", text)
    text = json.loads(text)
    name = text["msg"]["name"]

    # get oauth cookie
    print("3")
    cookie_str, text = get_oauth(cookie)
    cookie = merge_cookie(cookie, cookie_str)
    print("Cookie: ", cookie)
    # print("Res text: ", text)

    return cookie, name


def start_reserve(roomId, startTime, endTime, day, seatNum, cookie):
    # get seat select token
    print("4")
    token = get_seat_token(roomId, day, cookie)
    print("token", token)

    # gotcha
    print("5")
    text = gotcha(roomId, startTime, endTime, day, seatNum, token, cookie)
    print(text)

    return text


def start(uname, password, roomId, startTime, endTime, day, seatNum):
    cookie, _ = start_login(uname, password)

    start_reserve(roomId, startTime, endTime, day, seatNum, cookie)


if __name__ == '__main__':
    start(uname, password, roomId, startTime, endTime, day, seatNum)

