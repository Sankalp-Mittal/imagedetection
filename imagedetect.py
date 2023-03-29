import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
     ret, img = cap.read()
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     ret_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
     contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     for contour in contours:
          approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

          M = cv2.moments(contour)
          if M['m00'] != 0.0:
                x = int(M['m10']/M['m00'])
                y = int(M['m01']/M['m00'])
          if len(approx) == 3:
               shape = "Triangle"
               cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)
               cv2.putText(img, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
          elif len(approx) == 4:
               (x, y, w, h) = cv2.boundingRect(approx)
               ar = w / float(h)
               shape = "Square" if ar >= 0.95 and ar <= 1.05 else "Rectangle"
               cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)
               cv2.putText(img, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
          elif len(approx) == 5:
               shape = "Pentagon"
               cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)
               cv2.putText(img, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
          else:
               shape = "Circle"
            #    cv2.putText(img, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
          cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)
    #  print(shape)
     cv2.imshow("FRAME", img)
     cv2.waitKey(1)