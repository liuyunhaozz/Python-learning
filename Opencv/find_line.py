import cv2
import numpy as np

class COM:
    def __init__(self, port, baud):
        self.port = port
        self.baud = int(baud)
        self.open_com = None
        self.get_data_flag = True
        self.real_time_data = ''

    # return real time data form com
    def get_real_time_data(self):
        return self.real_time_data

    def clear_real_time_data(self):
        self.real_time_data = ''

    # set flag to receive data or not
    def set_get_data_flag(self, get_data_flag):
        self.get_data_flag = get_data_flag

    def open(self):
        try:
            self.open_com = serial.Serial(self.port, self.baud)
        except Exception as e:
            print("ERROR")

    def close(self):
        if self.open_com is not None and self.open_com.isOpen:
            self.open_com.close()

    def send_data(self, data):
        if self.open_com is None:
            self.open()
        success_bytes = self.open_com.write(data.encode('UTF-8'))
        return success_bytes
    def send_0x_data(self, data):
        if self.open_com is None:
            self.open()
        success_bytes = self.open_com.write(data.to_bytes(1, byteorder= 'big'))
        return success_bytes
    def get_data(self, over_time=30):
        pass
    def protocol(self, addr, use, data):
        sum = 0
        Sum_sum = 0
        #head
        success_bytes = self.open_com.write(0xAA.to_bytes(1, byteorder= 'big'))
        sum += 0xAA
        Sum_sum += sum
        #addr
        success_bytes &= self.open_com.write(addr.to_bytes(1, byteorder= 'big'))
        sum += addr
        Sum_sum += sum
        #function
        success_bytes &= self.open_com.write(use.to_bytes(1, byteorder= 'big'))
        sum += use
        Sum_sum += sum
        #length
        success_bytes &= self.open_com.write(len(data).to_bytes(1, byteorder= 'big'))
        sum += len(data)
        Sum_sum += sum
        #data
        for i in range(len(data)):
            success_bytes &= self.open_com.write(data[i].to_bytes(1, byteorder= 'big'))
            sum += data[i]
            Sum_sum += sum
        success_bytes &= self.open_com.write((sum & 0xFF).to_bytes(1, byteorder= 'big'))
        success_bytes &= self.open_com.write((Sum_sum & 0xFF).to_bytes(1, byteorder= 'big'))

ID = 1
cap = cv2.VideoCapture(ID)
#com = COM('/dev/ttyUSB0', 500000)
#com.open()
while True:
    _, img = cap.read()
    #print(img0.shape)
    #cv2.imshow("Original image", img0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#转灰度图

    gray = cv2.medianBlur(gray, 17)#模糊降噪
    ret, gray = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    #cv2.imshow('Fram', gray)
    kernel = np.ones((5, 5), np.uint8)
    dilate = cv2.dilate(gray, kernel, iterations=1)

    edges = cv2.Canny(dilate, 70, 150, apertureSize=3)
    #cv2.imshow("Cimg", dilate)
    lines = cv2.HoughLinesP(edges, 1, 1.0 * np.pi / 180, 40, minLineLength=5, maxLineGap=25)
    if lines is not None:
        X1 = Y1 = 1000
        X2 = Y2 = 0
        ry1 = 0
        ry2 = 0
        for (x1, y1, x2, y2) in lines[:, 0]:
            if(y1>250 or y1<230):
                continue
            #print(x1, y1, ";", x2, y2)
            #if abs(x1-x2)<2 & abs(y1-y2)>5:
            #cv2.line(img, (x1, 0), (x1, 480), (0, 0, 255), 3)
            if 320-x1<20 and 320-x2<20 and 320-x1>-20 and 320-x2>-20:
                cv2.line(img,(x1,0),(x1,480),(0,0,255),3)
    #            com.protocol(0x25, 0x01, [0])
                print(y1)
            if 320-x1 > 20:
                pass
                print('Left')
                print(x1-320)

     #           com.protocol(0x25, 0x01, [1,240-y1])
                # com.get_data(50)
            if 320-x1 < -20:
                pass
                print('Right')
                print(x1-320)
      #          com.protocol(0x25, 0x01, [1,240-y1])
                # com.get_data(50)



    else:
        pass
       # com.protocol(0x25, 0x01, [2])
            #cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)  # 画直线
        #cv2.line(img, (X1, Y1), (X2, Y2), (0, 0, 255), 3)  # 画直线
        #cv2.line(img, (0,0), (0,450), (0,0,255), 3)

    cv2.imshow("detection", img)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
       break