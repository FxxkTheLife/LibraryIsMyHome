import os
if not os.path.exists("./preset/time-slice.json"):
    print('新建json文件成功')
    fp = open("./preset/time-slice.json","w")
    fp.write("[]")
    fp.close()