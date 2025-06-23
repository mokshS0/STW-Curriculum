import cv2

# Step 1: Open the webcam
cap = cv2.VideoCapture(0)  # 0 means default camera

# Optional: Change resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Main loop: Show the camera feed
while True:
    ret, frame = cap.read()  # 'ret' checks if frame is read correctly, 'frame' holds the image

    # Filters to try:
    # 1. Grayscale
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. Flip horizontally
    # frame = cv2.flip(frame, 1)

    # 3. Blur effect
    # frame = cv2.GaussianBlur(frame, (15, 15), 0)

    # 4. Invert colors
    # frame = cv2.bitwise_not(frame)

    # Show the image in a window called 'frame'
    cv2.imshow('frame', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up: Close the camera and window
cap.release()
cv2.destroyAllWindows()
