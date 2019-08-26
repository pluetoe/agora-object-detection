from agora_community_sdk import AgoraRTC
from imageai.Detection import ObjectDetection
import os

client = AgoraRTC.create_watcher("dc96e5c14025414ea38980c9b1b1fbe4", "chromedriver.exe")
client.join_channel("meher")

users = client.get_users() # Gets references to everyone participating in the call

user1 = users[0] # Can reference users in a list

binary_image = user1.frame # Gets the latest frame from the stream as a PIL image

#with open("test.jpg") as f:
#    f.write(str(binary_image)) # Can write to file
binary_image.save("in.png") #Replace test.png with your file name
execution_path = os.getcwd() #Returns current working directory of the project

detector = ObjectDetection()   #Calls the object detection function from the library ImageAI
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5")) #make sure that you have downloaded resnet50_coco_best_v2.0.1.h5 to your main folder
detector.loadModel()

#detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "test.png"), output_image_path=os.path.join(execution_path , "test_output.png"))
detections, extracted_images = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "in.png"), output_image_path=os.path.join(execution_path , "out.png"), extract_detected_objects=True)
    #The above line not only just labels the objects in an image but also it extracts those images and saves it in a new directory

for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )

client.unwatch() #Ends the stream