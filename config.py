from config_init import Config_Init, TrafficSign_Init

RED_ZONE = 0
BLUE_ZONE = 1


class Config(Config_Init):
    DEBUG: bool = True
    LOOK_AT: int = RED_ZONE
    LANE_WIDTH: int = 160
    WIDTH: int = 320
    HEIGHT: int = 240

    CANNY_LOW: int = 25
    CANNY_HIGHT: int = 50

    LOW_H: int = 0
    LOW_S: int = 0
    LOW_V: int = 0

    HIGH_H: int = 180
    HIGH_S: int = 255
    HIGH_V: int = 100

    BG_SIGN: list = [150, 40, 40, 180, 255, 200]
    BLUE_SIGN: list = [105, 20, 20, 160, 200, 200]
    GREEN_SIGN: list = [5, 20, 20, 65, 180, 200]
    YELLOW_SIGN: list = [15, 40, 40, 30, 255, 200]
    CYAN_SIGN: list = [150, 40, 40, 180, 180, 200]
    VIOLET_SIGN: list = [150, 40, 40, 180, 180, 200]

    SIGN_LINE: int = 40

    SKY_LINE: int = 120

    ZONE: int
    WINDOW_WIDTH: int = 320
    WINDOW_HEIGHT: int = 240

    BTN1: int = 15
    BTN2: int = 7
    BTN3: int = 16
    BTN4: int = 12

    BL: int = 5
    LIGHT: int = 10
    SUB: int = 25

    softPWMLeft1: int = 21
    softPWMLeft2: int = 30
    softPWMRight1: int = 24
    softPWMRight2: int = 23

    STEER_SERVO: int = 12
    PROX_PIN: int = 14

    VELOCITY: float = 50.

    kP: float = 0.9
    kI: float = 0.1
    kD: float = 0.4


class TrafficSign(TrafficSign_Init):
    def __init__(self):
        self.my_sign = None

    @property
    def TurnLeft(self):
        self.my_sign = "TurnLeft"

    @property
    def TurnRight(self):
        self.my_sign = "Turnleft"

    @property
    def Change(self):
        self.my_sign = "Change"

    @property
    def Stop(self):
        self.my_sign = "stop"

    @property
    def Nothing(self):
        self.my_sign = None

    @property
    def Status(self):
        return self.my_sign


print(Config.DEBUG)
