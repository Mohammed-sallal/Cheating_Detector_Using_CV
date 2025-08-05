# Real-Time Gaze Tracking for Proctoring

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)

A computer vision project for real-time gaze tracking and cheating detection. It uses a webcam to monitor a user's eye movements and automatically saves an image when suspicious behavior is detected.

---

## Topics Covered

This project is a deep dive into real-time computer vision for proctoring, including:

-   **Facial Landmark Detection**: <br>
    Using dlib's pre-trained model to detect 68 key points on the user's face from a live webcam feed.

-   **Eye Isolation & Pupil Tracking**:
    -   Isolating the precise eye regions using facial landmarks.
    -   Applying image processing (bilateral filtering, erosion, and thresholding) to pinpoint the pupil.
    -   Calculating the pupil's centroid to determine its exact location.

-   **Automated Calibration**: <br>
    An initial calibration phase analyzes the first 20 frames to find the optimal binarization threshold, adapting to the user's specific eye features and current lighting conditions.

-   **Gaze Vector Analysis**:
    -   Calculating horizontal and vertical ratios based on the pupil's position within the eye frame.
    -   Translating these ratios into discrete directions: left, right, or center.

-   **Blink & Downward Gaze Detection**: <br>
    Calculating the eye-aspect-ratio to detect blinks. An extended blink (over 400ms) is interpreted as the user looking down.

-   **Automated Proctoring & Evidence Capture**: <br>
    If the system detects a left, right, or downward gaze, it automatically captures the current frame and saves it as a timestamped JPEG file for evidence.

---

## Project Structure

The project is organized into several key Python modules:

-   `gaze_tracking/`: The main package containing the core logic.
-   `gaze_tracking/gaze_tracking.py`: The main class that orchestrates face detection, eye analysis, and gaze direction.
-   `gaze_tracking/eye.py`: A class for isolating the eye and managing blinking detection.
-   `gaze_tracking/pupil.py`: Handles the detection and location of the pupil within the eye frame.
-   `gaze_tracking/calibration.py`: Manages the initial calibration process.
-   `trained_models/`: Contains the pre-trained dlib model for facial landmark detection.
-   `example.py`: A script demonstrating how to use the GazeTracking library.
-   `cheaters_detection/`: The default directory where captured images are saved.

---

**Requirements**
     - Python 3.x
     - OpenCV (`opencv-python`)
     - dlib
     - NumPy
