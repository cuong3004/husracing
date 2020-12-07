from abc import ABCMeta, abstractmethod
from config import TrafficSign


class DetectLane_Init:
    __metaclass__ = ABCMeta

    m_signDeteced = TrafficSign()

    @abstractmethod
    def getErrorAngle(self) -> float:
        pass

    @abstractmethod
    def HasLane(self) -> bool:
        pass

    @abstractmethod
    def IsStop(self) -> bool:
        pass

    # ---------------------
    @abstractmethod
    def preProcess(self):
        pass

    @abstractmethod
    def binaryImage(self):
        pass

    @abstractmethod
    def fitLane2Line(self):
        pass

    @abstractmethod
    def findLane(self):
        pass

    @abstractmethod
    def findSign(self):
        pass

    @abstractmethod
    def errorAngle(self) -> float:
        pass


class HoughLine_Init:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass


class Point_Init:
    def __init__(self):
        pass
