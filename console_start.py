from console_view.console_home import console_home

if __name__ == '__main__':
    try:
        console_home()
    except KeyboardInterrupt:
        print("正常退出")
