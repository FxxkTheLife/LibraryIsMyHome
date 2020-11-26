import os
if not os.path.exists("./preset/time-slice.json"):
    fp = open("./preset/time-slice.json",'w')
    fp.write("[]")
    fp.close()