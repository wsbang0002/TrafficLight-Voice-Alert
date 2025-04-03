from ultralytics import YOLO
import os

# 1. 모델 로드
model = YOLO("yolov10m.pt")  # YOLOv10 모델을 YOLOv14 엔진에서 사용 

# 2. 클래스 이름 매핑 (학습된 클래스에 따라 조정 가능)
class_names = ["red", "green", "yellow"]

# 3. 결과 파일 쓰기 함수
def write_result(new_label):
    if not os.path.exists("signal_result.txt") or open("signal_result.txt").read().strip() != new_label:
        with open("signal_result.txt", "w") as f:
            f.write(new_label)
        print(f"[UPDATED] signal_result.txt ← {new_label}")

# 4. 영상에서 실시간 탐지
results = model.predict(source="test_video.mp4", stream=True)

# 5. 탐지 결과 확인 및 기록
for result in results:
    if result.boxes.cls.numel() > 0:
        cls_id = int(result.boxes.cls[0])
        label = class_names[cls_id].upper()
        if label in ["RED", "GREEN"]:
            write_result(label)
        else:
            write_result("NONE")
    else:
        write_result("NONE")
