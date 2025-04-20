from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("./model/best.pt")


# Perform object detection on an image
results = model("./img/IMG_2199.jpg")  # Predict on an image
results[0].show()  # Display results
