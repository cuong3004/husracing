from abc import ABCMeta, abstractmethod


class CarControl_Init:
    __metaclass__ = ABCMeta

    m_steerAngle: float
    m_speed: int

    @abstractmethod
    def Init(self):
        pass

    @abstractmethod
    def SetSpeed(self, speed: int, bias: float = 0):
        pass

    @abstractmethod
    def Brake(self):
        pass

    @abstractmethod
    def SetSteerAngle(self, angle: float):
        pass

    @abstractmethod
    def EndCar(self):
        pass
