from ultralytics import YOLO
model = YOLO("model/yolo11n.pt")
if __name__ == "__main__":
    train_results = model.train(
        data="N:\\DEV\\python_image\\TrainModel\\datasets\\data.yaml",  #path folder file
        epochs=100,  
        imgsz=640,  
        device="cuda",  
    )
    metrics = model.val()




