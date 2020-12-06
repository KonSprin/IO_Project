import cv2
import os
import csv
import math
from time import time

from detections import detect

# Set variables
PATH = str(os.path.dirname(os.path.abspath(__file__))) + "\\"
FONT = cv2.FONT_HERSHEY_COMPLEX
COLOUR = (200,200,0)
current_skip = 0
first_start = time()
frame_number = 0
all_frames_log = []
# Input variables - theese should be passed down from GUI
INPUT_DIR = PATH + "videos\\test2.mp4"
LOG_DIR = "logs" + "\\" + INPUT_DIR.split('\\')[-1].split('.')[0] + '.csv'
do_skip = True  # Should we skip frames
skip = 4    # Default number of skipped frames. Can be adjusted depending on machine

OUTPUT_DIR = INPUT_DIR.split('.')[0] + '_output.' + INPUT_DIR.split('.')[1]

# Load yolo
net = cv2.dnn.readNet(PATH + "yolov3.weights", PATH + "yolov3.cfg")
classes = []
with open(PATH + "coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Load Video and set up output video
video = cv2.VideoCapture(INPUT_DIR)
VIDEO_FPS = video.get(cv2.CAP_PROP_FPS)
VIDEO_WIDTH = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
VIDEO_HEIGHT = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
VIDEO_CODEC =  int(video.get(cv2.CAP_PROP_FOURCC))
result = cv2.VideoWriter(OUTPUT_DIR, VIDEO_CODEC, VIDEO_FPS , (VIDEO_WIDTH, VIDEO_HEIGHT))                                 

start = time() # measure time for adjusting skipping frames
while frame_number < 150:
    frame_number += 1
    
    # Load image, frame by frame
    succes, img = video.read()
    if not succes:
        break

    #  showing info, skipping some frames for efficiency
    if current_skip == 0 or not do_skip:
        class_ids, confidences, boxes = detect(img, net)
        current_skip = skip
    current_skip -= 1

    frame_log = [] # all detections for one frame

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.6, 0.4) # NMSBoxes clears out theese boxes that are overlaping
    for i in indexes:
        i = int(i)
        if class_ids[i] in [0,1,2,3,5,6,7]: # detect only [person, bicycle, car, motorbike, bus, train, truck]
            x, y, width, height = boxes[i]

            # Diplay info for all detections
            label = classes[class_ids[i]].upper()
            conf = str(round(confidences[i] * 100,1)) + "%"
            cv2.rectangle(img, (x, y), (x + width, y + height), COLOUR, 2)
            cv2.putText(img, label, (x+5, y+15), FONT, 0.5,  COLOUR, 1)
            cv2.putText(img, conf, (x+5, y+height-5), FONT, 0.5,  COLOUR, 1)

            frame_log.append([frame_number, label, x, y, False])

    all_frames_log.append(frame_log)
        
    # show current frame in upper right corner
    cv2.putText(img, str(frame_number), (20, 20), FONT, 0.5,  COLOUR, 2)
    # write current frame
    result.write(img)

    # Function to dynamicly adjust number of skipped frames if speed is too low
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

# Logger function 
logger = []
car_id = 1
for n, frame in enumerate(all_frames_log):
    if n == 0:
        for car in frame:
            car[4] = car[0]/VIDEO_FPS
            car[0] = car_id
            if car[2] in ['PERSON', 'BICYCLE', 'BUS','TRAIN']:
                car[2] = 'OTHER'
            logger.append(car)
            car_id+=1
    else:
        for car in frame:
            for car_prev in all_frames_log[n-1]:
                dist = math.dist([car[2],car[3]],[car_prev[2],car_prev[3]])
                if dist < 100:
                    car[4] = True
            if not car[4]:
                car[4] = car[0]/VIDEO_FPS
                car[0] = car_id
                if car[2] in ['PERSON', 'BICYCLE', 'BUS','TRAIN']:
                    car[2] = 'OTHER'
                logger.append(car)
                car_id+=1


with open(LOG_DIR, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',',
                            quotechar='`', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['id', 'class', 'x_pos', 'y_pos', 'first appearance [s]'])
    for car in logger:
        writer.writerow(car)

video.release() 
result.release() 