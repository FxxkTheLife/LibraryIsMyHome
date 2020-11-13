import os
from update_check import checkForUpdates, update

directory = os.getcwd()
supported_version = ["", "0.4"]

remoteBaseURL = "http://cdn.jsdelivr.net/gh/FxxkTheLife/LibraryIsMyHome"
localBaseURL = os.getcwd()

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


def update_command():
    for file in file_to_update:
        update_file(file)


def update_file(file):
    global remoteBaseURL, localBaseURL
    localURL = localBaseURL + file
    remoteURL = remoteBaseURL + file
    if os.path.exists(localURL):
        checkForUpdates(localURL, remoteURL)
    else:
        update(localURL, remoteURL)


def start_update(version, new_version):
    if version not in supported_version:
        print("你当前版本不支持更新版本")
        return

    global remoteBaseURL, localBaseURL
    remoteBaseURL += "@" + new_version
    update_command()
    print("\033[32m👏👏🍺恭喜！更新已完成，欢迎使用新版本 {} ~~~\033[0m".format(new_version))
