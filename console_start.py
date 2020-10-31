from login import *
from reserve import *

from console_view.console_home import console_home

import sys

try:
    console_home()
except KeyboardInterrupt:
    print("正常退出")
    # sys.exit(0)

# start(uname, password, roomId, startTime, endTime, day, seatNum)
