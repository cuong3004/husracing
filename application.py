from application_init import Application_Init
import cv2
import time

def middle(value:float, min:float, max:float) -> float:

	if (value > max):
		value = max 
	elif (value < min):
		value = min 
	return value

class Application(Application_Init):
	def __init__(self):
		cv2.startWindowThread()
		# cv2.nameWindow("Camera", cv2.CV_WINDOW_AUTOSIZE)
	 #    namedWindow( "HSV Slider", CV_WINDOW_AUTOSIZE );
		# createTrackbar("LOW H", "HSV Slider", &Config::YELLOW_SIGN[0], 180);  #chon nguong mau cho vong tron bien phia trong
		# createTrackbar("HIGH H", "HSV Slider", &Config::YELLOW_SIGN[3], 180);  #BG_SIGN  chon nguong mau cho hinh bao ben ngoai
		# createTrackbar("LOW S", "HSV Slider", &Config::YELLOW_SIGN[1], 255);   #dieu chinh slide HSV de chon nguong cho BG_SIGN truoc
		# createTrackbar("HIGH S", "HSV Slider", &Config::YELLOW_SIGN[4], 255);  #dien vao trong config
		# createTrackbar("LOW V", "HSV Slider", &Config::YELLOW_SIGN[2], 255);
		# createTrackbar("HIGH V", "HSV Slider", &Config::YELLOW_SIGN[5], 255);
		# print(type(self.m_capture))

	def Start(self):
		image = ''
		# self.m_car.Init()

		# self.m_car.SetSteerAngle(30)
		time.sleep(1)
		# self.m_car.SetSteerAngle(0)

		# currentSign = TrafficSign()
		currentSign = None 
		signCountdown:int = 0
		start:bool = False 
		# wir.digitalWrite(Config.LIGHT, LOW)

		# bat camera
		cap = self.m_capture.Capture()

		while True:

			
			_, image = cap.read()
			# key:str = cv2.waitKey(1)
			# print(key == 27)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				return
			print("ok")
			cv2.imshow("Capture", image)
			# if (key == 'r'):
			# 	start = True 

			# if (wir.digitalRead(Config.BTN3) == wir.LOW):
			# 	time.sleep(1)
			# 	if (wir.digitalRead(Config.BTN3) == wir.LOW):
			# 		start = False 
			# 		break 
			# if (not start):
			# 	cv2.imshow("Camera", image)
			# 	if(wir.digitalRead(Config.BTN1) == wir.LOW):
			# 		start = True 
			# 		time.sleep(0.25)
			# 	continue

			# if (digitalRead(Config.PROX_PIN) = wir.LOW):
			# 	self.m_car.SetSpeed(0)
			# 	self.m_car.SetSteerAngle(0)
			# 	continue 

			self.m_detector.update(image)
		
