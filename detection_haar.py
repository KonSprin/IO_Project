import cv2
import tensorflow


cap = cv2.VideoCapture('D:/Projects/IO/IO_Project/videos/test.avi')
carCascade = cv2.CascadeClassifier("D:/Projects/IO/IO_Project/haar/car2.xml")

playSpeed = int(1000/8.33)

while True:
    succes, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = carCascade.detectMultiScale(imgGray, 1.1, 2)

    for (x,y,w,h) in cars:
        area = w*h
        # if area > 100:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(img, "CAR", (x+20,y+10), cv2.FONT_HERSHEY_PLAIN, 1, (0,250,0), 2)
            

    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break
