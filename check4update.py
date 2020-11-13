import os
import requests
from update_check import checkForUpdates, update
import ssl
ssl._create_default_http_context = ssl._create_unverified_context

directory = os.getcwd()
version_file_path = directory + "/version"
version_url = "https://raw.githubusercontent.com/FxxkTheLife/LibraryIsMyHome/main/version"
remote_url = "https://cdn.jsdelivr.net/gh/FxxkTheLife/LibraryIsMyHome"
file_path = directory + "/test.md"


def check4update(file, url):
    if os.path.exists(file):
        checkForUpdates(file, url)
    else:
        update(file, url)


def is_version_available(version):
    return requests.get(remote_url + "@" + version + "/README.md").status_code == 200


def get_new_version_update(version, new_version):
    try:
        response = requests.get(remote_url + "@{}/new_version_update.py".format(new_version))
    except ConnectionError:
        print("网络错误，请检查网络连接")
        raise KeyboardInterrupt
    if response.status_code == 200:
        command = response.text
        start_command = '\n\nstart_update("{}", "{}")'.format(version, new_version)
        return command + start_command
    else:
        print("获取错误")
        raise KeyboardInterrupt


def check_version():
    new_version = ""
    while True:
        input_str = input("由于 GitHub raw 国内被墙，可能无法自动检测更新，是否手动输入版本号[N/n]，或者继续使用自动更新[任意键]")
        if input_str == "N" or input_str == "n":
            while True:
                version_str = input("请输入版本号：")
                print("正在查询版本信息...")
                if is_version_available(version_str):
                    new_version = version_str
                    break
                print("无法获得此版本，请重新输入")
            break
        else:
            print("检查更新中...")
            try:
                response = requests.get(version_url)
            except ConnectionError:
                print("网络错误，请检查网络连接")
            if response.status_code == 200:
                new_version = response.text
                break
            print("检查更新失败")

    print("查询到版本 {}".format(new_version))
    with open(version_file_path, "r") as f:
        version = f.read()
        version = version.rstrip("\n")

    return version, new_version


def update_all(version, new_version):
    print("正在更新到版本 {}".format(new_version))
    exec(get_new_version_update(version, new_version), globals())


if __name__ == '__main__':
    try:
        version, new_version = check_version()

        if version == new_version:
            print("现已是此版本")
            input("回车退出")
            raise KeyboardInterrupt
        else:
            print("当前版本是 " + version + "，需要更新的版本是 " + new_version)
            input("回车继续")

        update_all(version, new_version)
    except KeyboardInterrupt:
        print("已退出")
