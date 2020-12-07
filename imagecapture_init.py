from abc import ABCMeta, abstractmethod 

class ImageCapture_Init:
	__metaclass__ = ABCMeta 

	def __init__(self):
		pass

	@abstractmethod
	def Capture(self):
		pass 
