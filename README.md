# Object Detection related projects.

1. Real time object detection.

Implementation of the file can be done in the following. The arguments are

video: path file video.
prototxt: network file is .prototxt
weights: network weights file is .caffemodel
thr: confidence threshold.

To execute the file:

python3 real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel

2. Save key events (still working on)

This program is expected to track a green ball and capture its motion, then save the motion clip in the folder named, output.Implementation of the file can be done in the following.

The key structure of the progam is

|--- output
|--- pyimagesearch
|    |--- __init__.py
|    |--- keyclipwriter.py
|--- save_key_events.py

In the pyimagesearch module, a class named KeyClipWriter is defined inside the keyclipwriter.py file.

To execute the file:

python3 save_key_events.py --output output

Credited to Adrian Rosebrock

3. Increase FPS

To execute the file:
 
 i) python3 writevideo.py
 or
 ii) python3 writevideo.py

4. TensorFlowLite Object Detection

The file and other documents are referrenced from  and credited to EdjeElectronics https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi.
