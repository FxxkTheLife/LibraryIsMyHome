def console_login(preset):
    if len(preset) > 0:
        while True:
            print("当前存在账号预设值：")

            print("+{}+{}+{}+".format("-" * 11, "-" * 15, "-" * 13))
            print("|{:^11}|{:^15}|{:^13}|".format("Choose", "User", "Name"))
            print("+{}+{}+{}+".format("-" * 11, "-" * 15, "-" * 13))
            i = 0
            for i, one in enumerate(preset):
                print("|{:^11}|{:^15}|{:^12}|".format(str(i + 1), one["uname"], one["name"] if "name" in one.keys() else ""))
            print("+{}+{}+{}+".format("-" * 11, "-" * 15, "-" * 13))
            try:
                res = int(input("是否使用账号预设值，是则输入序号，否则按 0："))
            except ValueError:
                continue
            else:
                if res == 0:
                    break
                if 1 <= res <= i + 1:
                    return preset[res - 1]["uname"], preset[res - 1]["password"], res - 1
    uname = input("请输入账号：")
    password = input("请输入密码：")
    return uname, password, None
