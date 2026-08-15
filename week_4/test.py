from ultralytics import YOLO
from pathlib import Path

dataset = Path(r"D:\Programming File\Datasets_for_my_practice\road_objects\Road-Anomalies-1")

model = YOLO("yolo11n.pt")

model.train(
    data=str(dataset / "data.yaml"),
    epochs=1,
    batch=8,
    workers=0,
    device=0
)