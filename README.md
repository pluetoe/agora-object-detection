# agora-object-detection

An object detection model build over the Agora's 1-to-1 video call. This model not only allows you to detect the objects over the call but also extract those objects as images.

# Prerequisites

1. Agora.io developer account (with app ID)
2. Python3

# Quick Start

Jump right into the code and see how to extract objects over agora's video call interface: 
1. Create an account on [agora.io](https://dashboard.agora.io). From the project manager create a new project and use the given app ID for this video call.
2. Open Object Detection folder and install all the python requirements through the terminal command 
'''bash
pip install -r requirements.txt
'''
3. Open ObjectDetection.py and paste your app ID over there along with a suitable channel name.
4. Download the yolo dataset from here(https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5) and paste it to the ObjectDetection directory
5. Now open a sample agora video call [channel](http://sidsharma27.github.io) and paste the same app ID and channel name over there and click join
6. Run ObjectDetection.py - this will take the frames from the video call and apply object detection using ImageAI. 
7. All the extracted objects can be seen in the folder named - "test_output.png-objects"
