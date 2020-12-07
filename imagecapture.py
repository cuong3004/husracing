from imagecapture_init import ImageCapture_Init
import cv2

class ImageCapture(ImageCapture_Init):
	def Capture(self):
		cap = cv2.VideoCapture(0)
		return cap

		