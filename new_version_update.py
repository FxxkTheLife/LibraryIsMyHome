import os
from update_check import checkForUpdates, update

directory = os.getcwd()
supported_version = ["0.4"]

remoteBaseURL = "https://cdn.jsdelivr.net/gh/FxxkTheLife/LibraryIsMyHome"
localBaseURL = ""


def update_file(file):
    global remoteBaseURL, localBaseURL
    localURL = localBaseURL + file
    remoteURL = remoteBaseURL + file
    if os.path.exists(localURL):
        checkForUpdates(localURL, remoteURL)
    else:
        update(localURL, remoteURL)


def update_command():
    update_file("/version")


def start_update(version, new_version):
    if version not in supported_version:
        print("你当前版本不支持更新版本")
        return

    global remoteBaseURL, localBaseURL
    remoteBaseURL += "@" + new_version
    update_command()
    print("版本 {} 更新已完成".format(new_version))
