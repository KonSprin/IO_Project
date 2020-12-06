import cv2
import numpy as np
import os
import csv
from time import time

from detections import detect, getColorName

# Set variables
PATH = str(os.path.dirname(os.path.abspath(__file__))) + "\\"
FONT = cv2.FONT_HERSHEY_COMPLEX
COLOUR = (200,200,0)
skip = 4
succes = True
current_skip = 0
do_skip = True
# Input variables
INPUT_DIR = PATH + "videos\\test2.mp4"
OUTPUT_DIR = INPUT_DIR.split('.')[0] + '_output.' + INPUT_DIR.split('.')[1]
LOG_DIR = "logs" + "\\" + INPUT_DIR.split('\\')[-1].split('.')[0] + '.csv'

# Load yolo
net = cv2.dnn.readNet(PATH + "yolov3.weights", PATH + "yolov3.cfg")
classes = []
with open(PATH + "coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Load Video
video = cv2.VideoCapture(INPUT_DIR)
result = cv2.VideoWriter(OUTPUT_DIR, int(video.get(cv2.CAP_PROP_FOURCC)), video.get(cv2.CAP_PROP_FPS) , 
                        (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))))                                 

first_start = start = time()
frame_number = 0
logger = []
while frame_number < 50:
    frame_number += 1
       
    # Load image
    succes, img = video.read()
    # img = cv2.resize(img, None, fx=0.5, fy=0.5)
    # img = cv2.imread(PATH + "videos\img.png")
    
    if succes == False:
        break

    # Uncomment to see how blob works
    # for b in blob:
    #     for n, image in enumerate(b):
    #         cv2.imshow(str(n), image)


    #  showing info
    if current_skip == 0 or not do_skip:
        class_ids, confidences, boxes = detect(img, net)
        current_skip = skip
    current_skip -= 1

    # indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.6, 0.4)
    for i in cv2.dnn.NMSBoxes(boxes, confidences, 0.6, 0.4):
        i = int(i)
        if class_ids[i] in [2,3,7]:
            x, y, width, height = boxes[i]

            # if detected:
            #     square = img[y:y+height,x:x+width]
            #     if len(square > 1):
            #         bgr = [0,0,0]
            #         num_pix = 0
            #         for row in square:
            #             for item in row:
            #                 bgr += item
            #                 num_pix += 1
            #         if num_pix > 0:
            #             b = int(bgr[0]/num_pix)
            #             g = int(bgr[1]/num_pix)
            #             r = int(bgr[2]/num_pix)

            label = classes[class_ids[i]].upper()
            conf = str(round(confidences[i] * 100,1)) + "%"
            cv2.rectangle(img, (x, y), (x + width, y + height), COLOUR, 2)
            cv2.putText(img, label, (x+5, y+15), FONT, 0.5,  COLOUR, 1)
            # cv2.putText(img, getColorName(b,g,r), (x+5, y+30), FONT, 0.5,  COLOUR, 1)
            cv2.putText(img, conf, (x+5, y+height-5), FONT, 0.5,  COLOUR, 1)

            logger.append([frame_number, label])
        
    cv2.putText(img, str(frame_number), (20, 20), FONT, 0.5,  COLOUR, 2)
    # cv2.imshow("Video", img)
    result.write(img)
    # print(frame_number, end='')

    if current_skip == 0 and frame_number > 30 and do_skip:
        time5f = time() - start
        print("mean fps for last " + str(skip) + " frames: " + str(skip/time5f))
        print("mean frames per sec: " + str(frame_number/(time() - first_start)))
        print("total frames processed: " + str(frame_number))
        if frame_number/(time() - first_start) < 5:
            skip += 1
            print("new skip: " + str(skip))
            current_skip = skip
        elif frame_number/(time() - first_start) > 6 and skip > 1:
            skip -= 1
            print("new skip: " + str(skip))
            current_skip = skip
        start = time()
    
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break

print("total time: " + str(time() - first_start))
print("mean frames per sec: " + str(frame_number/(time() - first_start)))

with open(LOG_DIR, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=' ',
                            quotechar='`', quoting=csv.QUOTE_MINIMAL)
    for row in logger:
        writer.writerow(row)

video.release() 
result.release() 
# Closes all the frames 
cv2.destroyAllWindows()