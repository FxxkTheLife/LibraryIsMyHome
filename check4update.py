import os
import requests
from update_check import checkForUpdates, update
import ssl
ssl._create_default_http_context = ssl._create_unverified_context

directory = os.getcwd()
version_file_path = directory + "/version"
version_url = "https://raw.githubusercontent.com/FxxkTheLife/LibraryIsMyHome/main/version"
remote_url = "https://cdn.jsdelivr.net/gh/FxxkTheLife/LibraryIsMyHome"


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
        print("\033[31m网络错误，请检查网络连接\033[0m")
        raise KeyboardInterrupt
    if response.status_code == 200:
        command = response.text
        start_command = '\n\nstart_update("{}", "{}")'.format(version, new_version)
        return command + start_command
    else:
        print("\033[31m数据获取错误，更新失败\033[0m")
        raise KeyboardInterrupt


def check_version():
    version = ""
    if os.path.exists(version_file_path):
        with open(version_file_path, "r") as f:
            version = f.read()
            version = version.rstrip("\n")
    while True:
        input_str = input("由于 GitHub raw 国内被墙，可能无法自动检测更新，是否手动输入版本号[N/n]，或者继续使用自动更新[任意键]")

        if input_str == "N" or input_str == "n":  # 手动
            while True:
                version_str = input("请输入版本号：")
                print("\033[34m正在查询版本信息...\033[0m")
                if is_version_available(version_str):
                    new_version = version_str
                    print("\033[32m查询到版本 {}\033[0m".format(new_version))
                    if version == new_version:
                        print("\033[32m当前已经是这个版本 {}\033[0m".format(version))
                        input("回车退出")
                        raise KeyboardInterrupt
                    else:
                        print("\033[32m当前版本 {} ====> 更新到版本 {}\033[0m".format(version, new_version))
                        input("回车开始更新 >>>")
                        return version, new_version
                print("\033[31m无法获得此版本，请重新输入\033[0m")

        else:  # 自动
            print("\033[34m检查更新中...\033[0m")
            try:
                response = requests.get(version_url)
            except ConnectionError:
                print("\033[31m网络错误，请检查网络连接\033[0m")
            if response.status_code == 200:
                new_version = response.text
                if version == new_version:
                    print("\033[32m检查完毕，当前已经是最新版本 {}\033[0m".format(version))
                    input("回车退出")
                    raise KeyboardInterrupt
                else:
                    print("\033[32m检查到有最新版本 {}\033[0m".format(new_version))
                    print("\033[32m当前版本 {} ====> 更新到版本 {}\033[0m".format(version, new_version))
                    input("回车开始更新 >>>")
                    return version, new_version
            print("\033[31m检查更新失败\033[0m")


def update_all(version, new_version):
    print("\033[34m正在更新到版本 {}...\033[0m".format(new_version))
    exec(get_new_version_update(version, new_version), globals())


if __name__ == '__main__':
    try:
        version, new_version = check_version()
        update_all(version, new_version)
    except KeyboardInterrupt:
        print("已退出")
