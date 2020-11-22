import cv2
import numpy as np
import os

# Set variables
PATH = str(os.path.dirname(os.path.abspath(__file__))) + "\\"
FONT = cv2.FONT_HERSHEY_COMPLEX
COLOUR = (200,200,0)

# Load yolo
net = cv2.dnn.readNet(PATH + "yolov3.weights", PATH + "yolov3.cfg")
classes = []
with open(PATH + "coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layers_names = net.getLayerNames()
layers_output = [layers_names[i[0]-1] for i in net.getUnconnectedOutLayers()]

# Load Video
video = cv2.VideoCapture(PATH + "videos\\test.avi")
result = cv2.VideoWriter(PATH + 'videos\\output.avi',  
                         cv2.VideoWriter_fourcc(*'MJPG'), 
                         10, (int(video.get(3)), int(video.get(4))) )

frame_number = 0

while frame_number < 50:
    frame_number += 1

    # Load image
    succes, img = video.read()
    # img = cv2.resize(img, None, fx=0.5, fy=0.5)
    # img = cv2.imread(PATH + "videos\img.png")
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, False)
    image_height, image_width, image_channels = img.shape
    net.setInput(blob)
    outs = net.forward(layers_output)

    # Uncomment to see how blob works
    # for b in blob:
    #     for n, image in enumerate(b):
    #         cv2.imshow(str(n), image)


    #  showing info

    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detevted
                center_x = int(detection[0] * image_width)
                center_y = int(detection[1] * image_height)
                width = int(detection[2] * image_width)
                height = int(detection[3] * image_height)

                #  Rectangle
                x = int(center_x - width/2)
                y = int(center_y - height/2)
                
                boxes.append([x, y, width, height])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.6, 0.4)
    for i in indexes:
        i = int(i)
        if class_ids[i] in [2,3,7]:
            x, y, width, height = boxes[i]
            label = classes[class_ids[i]].upper()
            conf = str(round(confidences[i] * 100,1)) + "%"
            cv2.rectangle(img, (x, y), (x + width, y + height), COLOUR, 2)
            cv2.putText(img, label, (x+5, y+15), FONT, 0.5,  COLOUR, 1)
            cv2.putText(img, conf, (x+5, y+height-5), FONT, 0.5,  COLOUR, 1)
        
    cv2.putText(img, str(frame_number), (20, 20), FONT, 0.5,  COLOUR, 2)
    # cv2.imshow("Video", img)
    result.write(img)
    print(frame_number, end='')
    
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break


video.release() 
result.release() 
    
# Closes all the frames 
cv2.destroyAllWindows()