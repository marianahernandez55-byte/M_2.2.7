from ultralytics import YOLO

if __name__ == '__main__':

    # Cargar el entrenamiento que se quedó en la época 40
    model = YOLO('runs/detect/train/weights/last.pt')

    # Continuar el entrenamiento
    results = model.train(
        resume=True,
        batch=4,
        device='0'
    )