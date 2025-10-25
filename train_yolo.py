from ultralytics import YOLO
import torch

DATA_YAML_PATH = 'data.yaml'
MODEL_WEIGHTS = 'yolov8n.pt'
BATCH_SIZE = 4
NUM_EPOCHS = 149
RUN_NAME = 'border_security_cpu_v1'


def train_custom_yolo():
    print("--- Starting YOLO Training Setup ---")

    print(f"PyTorch CUDA Available: {torch.cuda.is_available()}")
    DEVICE = 'cpu'
    print(f"Training Device Set to: {DEVICE}")

    model = YOLO(MODEL_WEIGHTS)
    print(f"Model {MODEL_WEIGHTS} loaded successfully.")

    print(f"\nTraining on {DEVICE} for {NUM_EPOCHS} epochs...")

    results = model.train(
        data=DATA_YAML_PATH,
        epochs=NUM_EPOCHS,
        imgsz=640,
        batch=BATCH_SIZE,
        name=RUN_NAME,
        device=DEVICE
    )

    print("\n--- Training Complete! ---")
    print(f"Results saved in the folder: runs/detect/{RUN_NAME}")


if __name__ == '__main__':
    train_custom_yolo()
