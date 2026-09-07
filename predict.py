from ultralytics import YOLO
import cv2


# Load trained weights
model = YOLO('runs/detect/train/weights/best.pt')


# Real-time inference execution
results = model.predict(source='1', show=True)