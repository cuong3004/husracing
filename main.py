from application import Application
from config import RED_ZONE, Config
import sys
import os


def main():
    app = Application()

    os.system("clear")

    arg = len(sys.argv)
    print(sys.argv)

    if arg >= 2:
        speed: int = sys.argv[1]
        print("Car Speed: ", speed)
    if arg >= 3:
        brightness: int = sys.argv[2]
        print("Brightness: ", brightness)
    if arg >= 4:
        zone = sys.argv[3]
        if zone == RED_ZONE:
            print("Zone: Red")
        else:
            print("Zone: Blue")
        Config.ZONE = zone

    app.Start()


if __name__ == '__main__':
    main()
