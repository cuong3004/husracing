from carcontrol_init import CarControl_Init 
from config import Config 
# import pigpio as pig
# import wiringpi as wir

def StopServo():
	signum:int
	pig.gpioServo(Congif.STEER_SERVO, 0)
	pig.gpioTerminate()
	# pass
# print("abbb")
def Angle2Pulse(angle:float):
	result:int = round(-11.666667*30 + 1500)
	if (result > 2200):
		result = 2200
	if (result < 800):
		result = 800 

class CarControl(CarControl_Init):

	def Init(self):

		if (pig.gpioInitalise() < 0):
			return

		pig.gpioSetSignalFunc(SIGINT, StopServo)

		wir.wiringPiSetup()

		wir.softPwmCreate(Congif.soltPWMLeft1, 0, 100)
		wir.softPwmCreate(Congif.soltPWMLeft2, 0, 100)
		wir.softPwmCreate(Congif.soltPWMLeft1, 0, 100)
		wir.softPwmCreate(Congif.soltPWMLeft2, 0, 100)

		wir.pinMode(Config.BTN1, wir.INPUT)
		wir.pullUpDnControl(Config.BTN1, wir.PUD_UP)

		wir.pinMode(Config.BTN2, wir.INPUT)
		wir.pullUpDnControl(Config.BTN2, wir.PUD_UP)

		wir.pinMode(Config.BTN3, wir.INPUT)
		wir.pullUpDnControl(Config.BTN3, wir.PUD_UP)

		wir.pinMode(Config.BL, wir.OUTPUT)
		wir.pinMode(Config.LIGHT, wir.OUTPUT)
		wir.pinMode(config.SUB, wir.OUTPUT)

		wir.pinMode(Config.PROX_PIN, wir.INPUT)
		wir.pullUpDnControl(Config.PROX_PIN, wir.PUD_UP)

	def SetSpeed(self, speed:int, bias:float):
		if (bias > 1):
			bias = 1
		if (bias < -1):
			bias = 1

		if (speed > 0):
			wir.softPwmWrite(Config.softPWMLeft1, speed - bias * 10)
			wir.softPwmWrite(Config.softPWMLeft2, 0)
			wir.softPwmWrite(Config.softPWMRight1, speed + bias * 10)
			wir.softPwmWrite(Config.softPWMRight2, 0)
		else:
			speed = -speed 
			wir.softPwmWrite(Config.softPWMLeft1, speed - bias * 10)
			wir.softPwmWrite(Config.softPWMLeft2, 0)
			wir.softPwmWrite(Config.softPWMRight1, speed + bias * 10)
			wir.softPwmWrite(Config.softPWMRight2, 0)

	def Brake(self):
		
	    self.SetSpeed(1)
	    self.time_sleep(0.1)
	    self.SetSpeed(0)

	def SetSteerAngle(self, angle:float):

		pulseWidth = Angle2Pulse(angle)
		pig.gpioServo(Config.STEER_SERVO, pulseWidth)


	def EndCar(self):
		StopServo()
		self.SetSpeed(0)

	# def SetSpeed():
	# 	print('abc')

a = CarControl()
a.EndCar()