import cv2
import os
import time
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

# Directory to save images of cheaters
save_dir = r"D:\pycharm files\eye motion project\cheaters detection"
os.makedirs(save_dir, exist_ok=True)  # Create the directory if it doesn't exist

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    # Check if the user is blinking more than 275ms (Looking down)
    blink_status = gaze.is_blinking()

    if blink_status == "Looking down":
        # If cheating is detected (looking down), take a picture and save it
        timestamp = time.strftime("%Y%m%d_%H%M%S")  # Unique timestamp for filename
        img_name = f"cheater_looking_down_{timestamp}.jpg"  # Name the image with a timestamp
        img_path = os.path.join(save_dir, img_name)

        # Save the image of the cheater
        cv2.imwrite(img_path, frame)
        print(f"Cheating detected! Saved image as {img_name}")  # For debugging purposes

    # Check if the user is looking to the right
    elif gaze.is_right():
        # If looking right, take a picture and save it
        timestamp = time.strftime("%Y%m%d_%H%M%S")  # Unique timestamp for filename
        img_name = f"cheater_looking_right_{timestamp}.jpg"
        img_path = os.path.join(save_dir, img_name)

        # Save the image
        cv2.imwrite(img_path, frame)
        print(f"Cheating detected! Saved image as {img_name}")  # For debugging purposes

    # Check if the user is looking to the left
    elif gaze.is_left():
        # If looking left, take a picture and save it
        timestamp = time.strftime("%Y%m%d_%H%M%S")  # Unique timestamp for filename
        img_name = f"cheater_looking_left_{timestamp}.jpg"
        img_path = os.path.join(save_dir, img_name)

        # Save the image
        cv2.imwrite(img_path, frame)
        print(f"Cheating detected! Saved image as {img_name}")  # For debugging purposes

    frame = gaze.annotated_frame()

    # Show the frame (without any text on it)
    cv2.imshow("Tracking window", frame)

    # Break the loop if the 'ESC' key is pressed
    if cv2.waitKey(1) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
