import cv2
import numpy as np
import pandas as pd

def detect(img, net):
    layers_names = net.getLayerNames()
    layers_output = [layers_names[i[0]-1] for i in net.getUnconnectedOutLayers()]

    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, False)
    image_height, image_width, image_channels = img.shape
    net.setInput(blob)
    outs = net.forward(layers_output)
    
    # #  Uncomment to see how blob works
    # for b in blob:
    #     for n, image in enumerate(b):
    #         cv2.imshow(str(n), image)

    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
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

    return class_ids, confidences, boxes