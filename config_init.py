from abc import ABCMeta, abstractmethod


class TrafficSign_Init:
    __metaclass__ = ABCMeta
    def __init__(self):
        self.m_sign = None

    @property
    @abstractmethod
    def Change(self):
        pass

    @property
    @abstractmethod
    def TurnLeft(self):
        pass

    @property
    @abstractmethod
    def TurnRight(self):
        pass

    @property
    @abstractmethod
    def Stop(self):
        pass

    @property
    @abstractmethod
    def Nothing(self):
        pass

    @property
    @abstractmethod
    def Status(self):
        pass


class Config_Init:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.DEBUG: bool
        self.LOOK_AT: int
        self.LANE_WIDTH: int
        self.WIDTH: int
        self.HEIGHT: int

        self.CANNY_LOW: int
        self.CANNY_HIGHT: int

        self.LOW_H: int
        self.LOW_S: int
        self.LOW_V: int

        self.HIGH_H: int
        self.HIGH_S: int
        self.HIGH_V: int

        self.BG_SIGN: list
        self.BLUE_SIGN: list
        self.GREEN_SIGN: list
        self.YELLOW_SIGN: list
        self.CYAN_SIGN: list
        self.VIOLET_SIGN: list

        self.SIGN_LINE: int

        self.ZONE: int
        self.WINDOW_WIDTH: int
        self.WINDOW_HEIGHT: int

        self.BTN1: int
        self.BTN2: int
        self.BTN3: int
        self.BTN4: int

        self.BL: int
        self.LIGHT: int
        self.SUB: int

        self.softPWMLeft1: int
        self.softPWMLeft2: int
        self.softPWMRight1: int
        self.softPWMRight2: int

        self.STEER_SERVO: int
        self.PROX_PIN: int

        self.VELOCITY: float

        self.kP: float
        self.kI: float
        self.kD: float
