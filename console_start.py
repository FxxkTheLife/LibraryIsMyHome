from backend.preliminary import detect_integrality
from console_view.console_home import console_home

if __name__ == '__main__':
    try:
        detect_integrality()
        console_home()
    except KeyboardInterrupt:
        pass
    print("\033[33m拜拜，下次见～\033[0m")
