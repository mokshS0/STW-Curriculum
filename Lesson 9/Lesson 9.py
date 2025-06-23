# === Load YOLO Model ===
import cv2
import numpy as np
import pyttsx3

# Load YOLOv4-tiny model and config file
net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg")

# Get layer names to understand how data flows through the model
layer_names = net.getLayerNames()

# Identify the output layers (needed to get detection results)
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]

# Load COCO class labels (e.g., person, bottle, car)
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# === Capture Frame and Create Input Blob ===
# Start video capture (0 = default camera)
cap = cv2.VideoCapture(0)

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 130)  # Optional: adjust speaking speed

print("Starting detection... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert image to a blob YOLO can use
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (320, 320), (0, 0, 0), True, crop=False)
    net.setInput(blob)  # Feed blob into the neural network
    outs = net.forward(output_layers)  # Run detection

    # === Process Output ===
    height, width, _ = frame.shape
    detected_labels = []

    for out in outs:
        for detection in out:
            scores = detection[5:]  # Probabilities for each class
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # Only continue if confidence is over 50%
            if confidence > 0.5:
                label = classes[class_id]

                # Get object box coordinates
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                # Draw rectangle and label
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} ({int(confidence*100)}%)", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Add to spoken list only once
                if label not in detected_labels:
                    detected_labels.append(label)

    # === Speak Detected Objects ===
    if detected_labels:
        sentence = "I see a " + " and a ".join(detected_labels)
        engine.say(sentence)
        engine.runAndWait()

    # Show frame
    cv2.imshow("Detection", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
