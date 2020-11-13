import os
import requests
import hashlib

supported_version = ["", "0.4"]

remoteBaseURL = "https://cdn.jsdelivr.net/gh/FxxkTheLife/LibraryIsMyHome"
localBaseURL = "."

dir_to_make = ["/backend/",
               "/console_view/",
               "/preset/"]

file_must_exist = [("/preset/login.json", "[]"),
                   ("/preset/seat.json", "[]")]

file_to_update = ["/backend/__init__.py",
                  "/backend/constant.py",
                  "/backend/cookie.py",
                  "/backend/login.py",
                  "/backend/my_seat.py",
                  "/backend/request.py",
                  "/backend/reserve.py",
                  "/backend/sign.py",
                  "/backend/start.py",
                  "/backend/supervise.py",
                  "/console_view/__init__.py",
                  "/console_view/console_home.py",
                  "/console_view/console_login.py",
                  "/console_view/input_booking_mess.py",
                  "/console_start.py",
                  "/console_start.command",
                  "/console_start.bat",
                  "/requirements.txt",
                  "/version"]


def isUpToDate(fileName, url):
    with open(fileName, "r") as f:
        file = f.read()
    hash = hashlib.sha256(file.encode('utf-8')).hexdigest()

    urlcode = requests.get(url).text
    urlhash = hashlib.sha256(urlcode.encode('utf-8')).hexdigest()

    if hash == urlhash:
        return True
    else:
        return False


def update(path, url):
    print("正在下载: {}".format(url))
    response = requests.get(url)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        with open(path, "w") as f:
            f.write(response.text)


def checkForUpdates(path, url):
    if not isUpToDate(path, url):
        update(path, url)
        return True
    else:
        return False


def update_file(file):
    global remoteBaseURL, localBaseURL
    localURL = localBaseURL + file
    remoteURL = remoteBaseURL + file
    if os.path.exists(localURL):
        checkForUpdates(localURL, remoteURL)
    else:
        update(localURL, remoteURL)


def update_dir(path):
    global localBaseURL
    localURL = localBaseURL + path
    if not os.path.exists(localURL):
        os.makedirs(localURL)


# 主命令
def update_command():
    global localBaseURL

    for path in dir_to_make:
        update_dir(path)
    for file in file_to_update:
        update_file(file)

    for file_info in file_must_exist:
        localURL = localBaseURL + file_info[0]
        if not os.path.exists(localURL):
            with open(localURL, "w") as f:
                f.write(file_info[1])


def start_update(version, new_version):
    if version not in supported_version:
        print("你当前版本不支持更新版本")
        return

    global remoteBaseURL, localBaseURL
    remoteBaseURL += "@" + new_version
    update_command()
    print("\033[32m👏👏🍺恭喜！更新已完成，欢迎使用新版本 {} ~~~\033[0m".format(new_version))
