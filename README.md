# A Gaze Guided virtual Mouse Interface
This project presents a virtual mouse system that allows users to control their computer using just their eyes. It uses OpenCV for video processing, MediaPipe for real-time facial landmark detection, and PyAutoGUI to move the mouse pointer and simulate clicks. The system is designed to provide a hands-free, accessible way to interact with a computer, especially useful for individuals with limited mobility or for innovative human-computer interaction projects.

The core idea is to track the user's eye movements using a webcam. MediaPipe's Face Mesh is used to detect facial landmarks, particularly around the eyes. By analyzing the relative position of the iris and eye shape, the system estimates the direction of the user's gaze. These gaze positions are then mapped to the screen coordinates, and PyAutoGUI is used to move the mouse cursor accordingly. Optionally, blink detection can be integrated to simulate mouse clicks.

To run this project, make sure you have Python 3.7 or above installed. You'll also need to install the required libraries: OpenCV, MediaPipe, and PyAutoGUI. You can do this easily using pip:

## pip install opencv-python mediapipe pyautogui

Once the dependencies are installed, simply run the main Python script to launch the application. Make sure your webcam is connected and enabled. The program will start capturing your face and tracking your eye movements to move the mouse cursor on your screen in real time.

This project is lightweight and works entirely on the CPU, making it suitable for most laptops and desktops without requiring a GPU. However, for best results, make sure you're in a well-lit environment and stay relatively still in front of the webcam. Since precise gaze tracking is a challenging task, some level of calibration or improvement may be needed depending on your hardware.
Assistive Technology: Empower individuals with physical disabilities to use computers independently.

Hands-Free Computing: Useful for scenarios where hands are occupied or contactless interaction is preferred (e.g., healthcare, cleanrooms).

Education and Research: Serves as a base for academic projects related to Human-Computer Interaction (HCI), Computer Vision, or Accessibility.

Gaming and AR/VR: Offers an innovative way to control interfaces with eye movements in immersive environments.
## How It Works: System Architecture
Webcam Input: Continuously captures live video frames.

# Facial Landmark Detection: 
Uses MediaPipe’s Face Mesh model to detect facial features, focusing on the eyes.

 # Gaze Estimation:
  Analyzes eye shape and iris location to infer gaze direction (left, right, up, down).

#  Cursor Mapping: 
Translates gaze direction into corresponding screen coordinates.

# Mouse Control: 
Moves the cursor with PyAutoGUI; optional eye blink detection can simulate clicks.

