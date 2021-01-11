# IO_Project
#### Simple application to detect cars in videos from cameras over the road.


## Setup
1. Required dependencies - numpy, PySide2, opencv-python, panadas \
 ```pip install numpy opencv-python pyside2 pandas``` \
 **or** \
 ```pip install -r requirements.txt```

2. Download [this file](https://pjreddie.com/media/files/yolov3.weights) and put it in main folder.
3. Create logs and videos folder (~~Or don't~~)
4. You are good to go 

## User manual
1. First you need to choose the destination folder fo log files
2. Chose video to process 
3. It'll be saved in same folder when it's finished processing
4. After it's done you can save the log file and/or play processed video

## Log file format 
It's a .csv file formatted like this:

 | *ID* | *Class* | *Position X* | *Position Y* | *Firts appearance [s]* |
 | --- | --- | --- | --- | ---- |
 |  1  | CAR | 979 | 92  | 0.12 |
 |  2  |OTHER| 725 | 593 | 9.96 |