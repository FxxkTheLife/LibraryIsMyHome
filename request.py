import requests
from constant import *


# GET request
def get_req(url, cookie=None):
    headers = {
        "User-Agent": user_agent
    } if cookie is None else {
        "User-Agent": user_agent,
        "Cookie": cookie
    }
    return requests.request("GET", url, headers=headers)


# GET request - return cookie, text
def get_req_to_cookie(url, cookie=None):
    response = get_req(url, cookie)
    return response.headers['Set-Cookie'], response.text
