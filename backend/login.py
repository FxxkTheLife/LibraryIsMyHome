import re

from backend.request import *
from backend.cookie import *


# login
def login(uname, password):
    url = "http://passport2-api.chaoxing.com/v11/loginregister?code=" + password + "&cx_xxt_passport=json&uname=" + uname + "&loginType=1&roleSelect=true"

    return get_req_to_cookie(url)


# get oauth cookie
def get_oauth(cookie=None):
    def get_oauth_token(cookie):
        url = "http://office.chaoxing.com/front/user/login/access?targetUrl=http%3A%2F%2Foffice.chaoxing.com%2Ffront%2Fapps%2Fseat%2Findex%3FfidEnc%3D321a0e36ee4a9fd1"

        cookie_res, text = get_req_to_cookie(url, cookie)

        res = re.search('oauth\.loadInfo\(\'[A-Za-z0-9]*\'\)', text)
        token = text[res.span()[0]: res.span()[1]].split("'")[1]
        print("token: ", token)

        res = re.search('webUrl: \'.*\'', text)
        next_url = text[res.span()[0]: res.span()[1]].split("'")[1]
        print("url: ", next_url)

        return cookie_res, token, next_url

    def get_oauth_cookie(uid, deptid, token, cookie, next_url):
        url = "http://office.chaoxing.com/front/user/login/dologin?uid=" + uid + "&deptid=" + deptid + "&token=" + token

        cookie_res, text = get_req_to_cookie(url, cookie)
        cookie = merge_cookie(cookie, cookie_res)
        print("Cookie: ", cookie)
        print("Res: ", text)

        return get_req_to_cookie(next_url, cookie)

    cookie_res, token, next_url = get_oauth_token(cookie)
    cookie = merge_cookie(cookie, cookie_res)
    cookie_dict = cookie2dict(cookie)
    fid = cookie_dict["fid"] if "fid" in cookie_dict.keys() else "0"
    return get_oauth_cookie(cookie_dict["UID"], fid, token, cookie, next_url)

