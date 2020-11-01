
def cookie2dict(cookie: str):
    cookie_dict = {}
    cookie = cookie.replace(",", ";")
    cookies = cookie.split(";")
    for one_cookie in cookies:
        one_cookie = one_cookie.split("=")
        if len(one_cookie) < 2:
            continue
        cookie_dict[one_cookie[0].strip()] = one_cookie[1].strip()
    return cookie_dict


def dict2cookie(cookie_dict: dict):
    cookie_str = ""
    for cookie in cookie_dict.items():
        cookie_str += cookie[0] + "=" + cookie[1] + "; "
    return cookie_str[:-2]


def merge_cookie(cookie1, cookie2):
    cookie1_dict = cookie2dict(cookie1)
    cookie2_dict = cookie2dict(cookie2)
    cookie1_dict.update(cookie2_dict)
    return dict2cookie(cookie1_dict)
