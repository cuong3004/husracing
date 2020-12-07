from abc import ABC

from detectlane_init import DetectLane_Init, HoughLine_Init, Point_Init
from config import Config

import cv2
import numpy as np
import math
import copy


def swap(a: int, b: int):
    temp: int = a
    a = b
    b = temp


def converLine(linesAll):
    lines = []
    for i in range(len(linesAll)):
        lines.append(linesAll[i, 0])

    return np.array(lines)



# tinh do dai doan thang
def lineLength(line) -> float:
    return math.sqrt((line[0] - line[2]) * (line[0] - line[2]) + (line[1] - line[3]) * (line[1] - line[3]))


# tinh goc nghiem duong thang
def lineAngle(line) -> float:
    X: float = line[2] - line[0]
    Y: float = line[3] - line[1]
    angle: float = math.atan(Y / X) * 180 / math.pi
    if angle > 90:
        angle -= 180
    if angle < -90:
        angle += 180
    return angle


# tinh khoang cach giua 2 diem 
def distance(x1: float, y1: float, x2: float, y2: float):
    return math.sqrt((x1 - x2) * (x1 - x2) + + (y1 - y2) * (y1 - y2))


# lay toa do x cua 2 mp thuoc duong thang
def getPoinInLine(line, y):
    point = Point()
    point.x = (y - line[1]) * (line[0] - line[3]) + line[0]
    point.y = y

    return point


# xac dinh xem hai vector co giao nhau hay khong


def isIntersect(line):
    a, b = HoughLine(frame, kind=2)
    head1: int = getPoinInLine(a, Config.HEIGHT / 2).x
    head2: int = getPoinInLine(b, Config.HEIGHT / 2).x
    tail1: int = getPoinInLine(a, Config.HEIGHT).x
    tail2: int = getPoinInLine(b, Config.HEIGHT).x
    if (head1 > head2 and tail1 < tail2) or (head1 < head2 and tail1 > tail2) or (
            abs(head1 - head2) < Config.LANE_WIDTH / 2):
        return True
    else:
        return False


# xem cp phai duong thang ko
def dist1(a, b):
    angle1: float = lineAngle(a)
    angle2: float = lineAngle(b)
    dist: float = min(distance(a[0], a[1], b[0], b[1]),
                      distance(a[2], a[3], b[2], b[3]))
    dist = min(dist, distance(a[0], a[1], b[2], b[3]))
    dist = min(dist, distance(a[2], a[3], b[0].b[1]))

    return (abs(angle1 - angle2) < 5) and (dist < 50)


def dist2(a, b):
    angle1: float = lineAngle(a)
    angle2: float = lineAngle(b)
    dist: float = min(distance(a[0], a[1], b[0], b[1]),
                      distance(a[2], a[3], b[2], b[3]))
    dist = min(dist, distance(a[0], a[1], b[2], b[3]))
    dist = min(dist, distance(a[2], a[3], b[0].b[1]))

    return (abs(angle1 - angle2) < 5) and (dist < 50)


# result =
# return result

class DetectLane(DetectLane_Init, ABC):
    def __init__(self):
        # self.m_signDetect = None
        # self.m_signDetected = None
        self.m_carPos = Point()
        self.m_carPos.x = Config.WIDTH / 2
        self.m_carPos.y = Config.HEIGHT

    # self.m_preLane = HoughLine()

    def update(self, src):
        output = copy.deepcopy(src)

        # binary = self.preProcess(output)

        lines = self.fitLane2Line(output)

    # self.findLane
    def findSign(self, src):
        MinSignArea: int = 500
        img = copy.deepcopy(src)
        img = cv2.medianBlur(img, 3)
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        signMask = cv2.inRange(imgHSV, (Config.BG_SIGN[0], Config.BG_SIGN[1], Config.BG_SIGN[2]),
                               (Config.BG_SIGN[3], Config.BG_SIGN[4], Config.BG_SIGN[5]))
        signMask1 = cv2.inRange(imgHSV, (0, 40, 80), (5, 140, 140))

        signMask = cv2.bitwise_or(signMask, signMask1)

        if np.count_nonzero(signMask) < MinSignArea:
            self.m_signDetected = None

            return

    def preProcess(self, src):
        pass

    def fitLane2Line(self, src):

        lines = HoughLine()
        lines = lines.getline(src)
        if lines is None:
            return
        print("linessss", lines.shape)
        # print("len ", len(lines))
        # for i in range(len(lines)):
        #     print(i)
        #     # { // Chỉ xét các đường nằm trên đường chân trời.
        #     # print()
        #     if lines[i][1] < Config.SKY_LINE:
        #         print(lines[i][1])
        #         print(i)
        #         if lines[i][3] < Config.HEIGHT / 3 * 2:
        #             continue
        #
        #     if lines[i][3] < Config.SKY_LINE:
        #         if lines[i][1] < Config.HEIGHT / 3 * 2:
        #             continue
        #     # print(lines[i])
        #     angle: float = lineAngle(lines[i])
        #
        #     if abs(angle) < 15:
        #         #  Chỉ xét các đường có góc nghiêng lớn hơn 15
        #         lines.pop(i)
        #         continue
        #
        #     if lines[i][1] < lines[i][3]:
        #         swap(lines[i][0], lines[i][2])
        #         swap(lines[i][1], lines[i][3])
        return lines


# xac dinh xem cac duong co phai duong hay khong


# tim duong thang
# Thuat toan phat hien duong thang
class HoughLine(HoughLine_Init):

    def thresholdImg(self, img):
        # doi he mau hsv

        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Lọc màu bằng HCV
        imgThresholded = cv2.inRange(imgHSV, (Config.LOW_H, Config.LOW_S, Config.LOW_V),
                                     (Config.HIGH_H, Config.HIGH_S, Config.HIGH_V))
        # khu nhieu
        element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5), (2, 2))
        imgThresholded = cv2.morphologyEx(imgThresholded, cv2.MORPH_OPEN, element, (2, 2))
        imgThresholded = cv2.dilate(imgThresholded, element, (2, 2))
        cv2.rectangle(imgThresholded, (70, 220), (270, 240), 0, thickness=-1)

        return imgThresholded

    def debug(self, imgThresholded):
        if Config.DEBUG:
            cv2.imshow("Threshold", imgThresholded)

    def getline(self, src):
        # print("src", src.shape)
        img = copy.deepcopy(src)
        # doi he mau GaussianBlur
        img = cv2.GaussianBlur(img, (3, 3), 0)

        # lay anh nguong
        imgThresholded = self.thresholdImg(img)

        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

        # Apply edge detection method on the image
        candyImg = cv2.Canny(gray, Config.CANNY_LOW, Config.CANNY_HIGHT)
        edges = cv2.bitwise_or(src1=candyImg, src2=candyImg, mask=imgThresholded)

        # DEBUG
        self.debug(edges)

        # This returns an array of r and theta values
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 20, 10, 7)

        # print("ssss", lines.shape)
        lines = converLine(lines)
        # xe tu lai
        # HoughLinesP(src, lines, 1, CV_PI / 180, 20, 10, 7)

        # The below for loop runs till r and theta values
        # are in the range of the 2d array
        # lines = []
        # print(len(lines))
        # lineAll = []
        # print(lines[0])

        for line in lines:
            cv2.line(img, (line[0], line[1]), (line[2], line[3]), (255, 0, 0))

        cv2.imshow("Hello", img)
        # print('abc',len(lineAll))

        return lines


# tao diem
class Point(Point_Init):
    def __init__(self):
        super().__init__()
        self.x: int
        self.y: int
