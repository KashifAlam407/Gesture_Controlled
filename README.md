# Gesture Controlled Projects (MediaPipe + Arduino)

This repository is a collection of gesture-controlled projects combining **MediaPipe (Python/OpenCV)** with **Arduino**. The goal is to provide a learning + implementation hub: first explore the concepts (class trees, visualization, serial comm), then try working projects (hand, thumb, face, eye detection). Each project folder contains both Python and Arduino code, so you can run them end-to-end.

---

## 📂 Repository Structure

```
gesture-control/
│
├── docs/                    # documentation, class trees, images
│   ├── mediapipe-tree.md     # class structure and explanation of MediaPipe Hands etc.
│   ├── opencv-basics.md      # OpenCV essential functions
│   ├── serial-communication.md # how Python ↔ Arduino serial works
│   ├── images/
│   │   ├── mediapipe_hand_tree.png
│   │   ├── landmarks_example.png
│   │   └── opencv_flow.png
│   └── diagrams/
│       └── python-arduino-flow.png
│
├── projects/                 # gesture based projects
│   ├── hand-detection/
│   │   ├── python/
│   │   │   └── hand_detection_code.py
│   │   ├── arduino/
│   │   │   └── serial_receiver.ino
│   │   └── README.md
│   │
│   ├── thumb-detection/
│   │   ├── python/
│   │   │   └── thumb_detection.py
│   │   ├── arduino/
│   │   │   └── thumb_control.ino
│   │   └── README.md
│   │
│   ├── face-detection/
│   │   ├── python/
│   │   │   └── face_detect.py
│   │   ├── arduino/
│   │   │   └── face_servo.ino
│   │   └── README.md
│   │
│   └── eye-detection/
│       ├── python/
│       │   └── eye_tracking.py
│       ├── arduino/
│       │   └── eye_control.ino
│       └── README.md
│
├── LICENSE
└── README.md                # (this file)
```

---

## 🖼️ Hand Landmarks Overview

MediaPipe’s hand detection identifies **21 keypoints** per hand. A sample landmark visualization (e.g. `docs/images/landmarks_example.png`) shows points like wrist, thumb tip, index tip, etc.  
Each point gives:  
- `x, y` → normalized image coordinates (0–1)  
- `z` → relative depth (negative values = closer to camera)

---

## 🌳 MediaPipe Hands Module — Tree + Explanation

```
mediapipe.solutions.hands
   └── Hands (class)
         ├── __init__(...)           # construct the pipeline: parameters like static_image_mode, max_num_hands, detection & tracking confidence
         └── process(image)           # run hand detection + landmark estimation on the input image
                ↓
             results (object)
                ├── multi_hand_landmarks              # list of hand landmarks (21 points per detected hand)
                ├── multi_handedness                  # classification of each detected hand as “Left” or “Right”
                └── multi_hand_world_landmarks        # 3D world coordinates (in meters) of the same landmarks
```

**What each part does:**
- `Hands(...)` initializes the hand detection + tracking model with given settings.  
- `process(image)` takes an RGB (or BGR converted) frame and returns `results`.  
- `multi_hand_landmarks` lets you access 2D normalized (x, y, z) points for each hand.  
- `multi_handedness` helps you know which hand is left or right.  
- `multi_hand_world_landmarks` is useful if you want real-world depth data for robotics/AR.

---

## 🌳 Drawing Utilities — Tree + Explanation

```
mediapipe.solutions.drawing_utils
   ├── draw_landmarks(image, landmark_list, connections, …)    # draw landmarks + lines on an image (OpenCV)
   ├── DrawingSpec (class)                                      # defines styles (color, thickness, radius) for drawing
   ├── plot_landmarks(landmark_list, connections, …)             # 3D plotting (matplotlib)
   └── Predefined Connection Sets
         ├── mp.solutions.hands.HAND_CONNECTIONS
         ├── mp.solutions.pose.POSE_CONNECTIONS
         └── mp.solutions.face_mesh.FACEMESH_* etc.
```

**Explanation:**
- Use `draw_landmarks()` to overlay points & lines onto your image frame for visualization.  
- `DrawingSpec` allows customizing how those points/lines appear.  
- `plot_landmarks()` is for 3D views (not commonly used for real-time OpenCV display).  
- Connection sets (like `HAND_CONNECTIONS`) define which landmarks should be connected (e.g. wrist → finger joints).

---

## 🚦 How the System Works (Workflow)

1. **Arduino Setup**  
   - Upload the sketch `serial_receiver.ino` (found in `projects/hand-detection/arduino/`).  
   - Arduino listens to incoming serial commands (e.g. identifiers like `"GESTURE_1"`) and drives servos, LEDs, or motors accordingly.

2. **Python Side**  
   - Run `hand_detection_code.py` in `projects/hand-detection/python/`.  
   - What it does:
   > a. Capture video frames from webcam (OpenCV)  
   > b. Use MediaPipe Hands to get landmarks  
   > c. Analyze positions (for example: if index_tip y < pip y → finger extended)  
   > d. Send a command string over serial to Arduino (e.g. `"INDEX_UP"`)  

3. **Data Flow Diagram**  
   (See `docs/diagrams/python-arduino-flow.png`)  
   Webcam → MediaPipe → Gesture logic → Serial command → Arduino → Hardware action  

---

## 🎯 Usage Instructions (Step by Step)

### Prerequisites
- Python 3.8 or above  
- Arduino IDE  
- Libraries:
```bash
pip install opencv-python mediapipe pyserial
```

### Steps
1. Connect your Arduino to your computer via USB.  
2. In the Arduino IDE, open `serial_receiver.ino` and upload it to the Arduino board.  
3. Note the serial port (e.g. `COM3` on Windows, `/dev/ttyUSB0` on Linux).  
4. In your terminal, go to `projects/hand-detection/python/` and run:
   ```bash
   python hand_detection_code.py
   ```
5. Show your hand in front of the camera. The Python script reads landmarks, infers a gesture, sends a command via serial. Arduino receives that command and performs the corresponding action (e.g. move servo).  

---

## 🔄 Extending & Customizing

- Add more gestures in the Python logic (analyze different sets of landmarks).  
- Update Arduino sketch to map more command strings to new actions (motors, relays, LEDs).  
- Use `multi_hand_world_landmarks` for depth-sensitive gestures (e.g. moving hand forward/back).  
- Create new project subfolders (`thumb-detection`, `face-detection`) following the same pattern.

---

## 📜 License & Contribution

This project is open source (add your LICENSE file, e.g. MIT).  
Feel free to fork, contribute new projects, improve documentation, and submit pull requests.

---

## 🔗 Useful References

- MediaPipe Hands Documentation  
- OpenCV Documentation  
- PySerial Documentation

---

> 💡 Tip: Always test your serial port connection (baud rate, line endings) before running full pipeline.

