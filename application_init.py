from abc import ABCMeta, abstractmethod

from imagecapture import ImageCapture
from detectlane import DetectLane
# from carcontrol import CarControl 

class Application_Init:
	__metaclass__ = ABCMeta

	def __init__(self):
		pass

	m_capture = ImageCapture()
	m_detector = DetectLane()
	# m_car = CarControl()

	m_integral:float = 0.
	m_preError:float


