Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from ultralytics import YOLO
... import os
... 
... model = YOLO("yolov10m.pt")
... class_names = ["red", "green", "yellow"]
... 
... def write_result(label):
...     with open("signal_result.txt", "w") as f:
...         f.write(label)
... 
... results = model.predict(source="test_video.mp4", save=True, save_txt=True, stream=True)
... 
... for result in results:
...     if result.boxes.cls.numel() > 0:
...         cls_id = int(result.boxes.cls[0])
...         label = class_names[cls_id].upper()
...         if label in ["RED", "GREEN"]:
...             write_result(label)
...         else:
...             write_result("NONE")
...     else:
...         write_result("NONE")
