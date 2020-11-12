import os
import requests
from update_check import checkForUpdates, update

directory = os.getcwd()
version_file_path = directory + "/version"
version_url = "https://raw.githubusercontent.com/FxxkTheLife/LibraryIsMyHome/main/version"
file_path = directory + "/test.md"


def check4update(file, url):
    if os.path.exists(file):
        checkForUpdates(file, url)
    else:
        update(file, url)


def check_version():
    print("检查更新中...")
    input_str = input("由于 GitHub raw 国内被墙，可能无法自动检测更新，是否手动输入版本号[Y/y]，或者继续使用自动更新[任意键]")
    with open(version_file_path, "r") as f:
        version = f.read()
    print(version)
    new_version = requests.get(version_url).text
    print(new_version)
    if version == new_version:
        print("现已是最新版本")
    else:
        print("当前版本是 " + version + "，最新版本是 " + new_version)


check4update(file_path, "https://cdn.jsdelivr.net/gh/FxxkTheLife/LibraryIsMyHome@0.4/README.md")

if __name__ == '__main__':
    check_version()
