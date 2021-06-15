import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    r,frame=cap.read()
    # decreasing noise

    blur = cv2.GaussianBlur(frame, (35, 35), 0)


    # decreasing noise
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 20, 70])
    upper_skin = np.array([20, 255, 255])

    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    contour, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #print(contour)

    # finding out maximum area
    for c in contour:
        area=cv2.contourArea(c)
        print(area)


        if area>1300:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)  # for showing all contours we have to give -1 as value

    cv2.imshow("blur",blur)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1)==ord('q'):          # cv2.waitKey(10000)  # 1347.5
        break


cap.release()
cv2.destroyAllWindows()