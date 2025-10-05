# ✋ Hand Detection Project (MediaPipe + Arduino)

This project demonstrates **real-time hand detection** using **MediaPipe Hands + OpenCV** in Python, and sending **serial commands to Arduino** to control hardware (like servos, LEDs, motors).  
It also includes a **practice code** so learners can experiment with different landmark logics before integrating with Arduino.

---

## 📂 Project Structure

```
hand-detection/
│
├── python/
│   ├── hand_detection_code.py    # Main code: detects hand & sends serial commands
│   ├── practice_code.py          # Practice code for experimenting with landmarks
│   └── utils.py (optional)       # helper functions if needed
│
├── arduino/
│   └── serial_receiver.ino       # Arduino sketch to read serial data & control servo
│
├── docs files
│
└── README.md                     # You are here
```

---

## 🖼️ Hand Landmarks

MediaPipe detects **21 landmarks per hand**.  
Each landmark has `(x, y, z)` coordinates:

- **x, y** → normalized (0–1) w.r.t. image width/height  
- **z** → depth (negative = closer to camera)

Example landmark map:  

![Hand Landmarks](docs/images/hand_landmarks.png)

---

## ⚙️ How It Works

### 1. Arduino Side
- Upload `serial_receiver.ino` to Arduino.  
- It listens on the **Serial port** for incoming messages like:
  ```
  INDEX_UP
  THUMB_DOWN
  GRAB
  ```
- Based on the message → move servo, turn on LED, or perform action.

### 2. Python Side
- Run `hand_detection_code.py`.  
- Steps:
  1. Capture webcam feed (`cv2.VideoCapture`).  
  2. Detect hand landmarks using **MediaPipe Hands**.  
  3. Compare landmark positions (e.g., `index_tip.y < index_pip.y` → finger up).  
  4. Send the command string to Arduino using **PySerial**.

### 3. Data Flow

```
Webcam → MediaPipe (Python) → Landmark Detection → Serial Command → Arduino → Hardware Action
```

---

## 🚀 Running the Project

### Requirements
- Python 3.8+
- Arduino UNO/Nano/compatible
- Dependencies:
  ```bash
  pip install opencv-python mediapipe pyserial
  ```

### Steps
1. **Connect Arduino**  
   - Open Arduino IDE  
   - Upload `serial_receiver.ino` to board  

2. **Find Arduino Port**  
   - Windows → `COM3`, `COM4`, …  
   - Linux/Mac → `/dev/ttyUSB0` or `/dev/ttyACM0`

3. **Run Python Detection**
   ```bash
   python python/hand_detection_code.py
   ```
4. **Test**  
   - Show hand gestures in front of webcam  
   - Arduino receives commands & reacts in real-time 🎉  

---

## 🧪 Practice Code

`practice_code.py` is included for learners:  
- Runs hand detection  
- Prints raw landmarks and finger positions in console  
- Helps you understand how to create new gestures before linking to Arduino  

Example experiment:
```python
if index_tip.y < index_pip.y:
    print("Index Finger Up")
```

---

## 🔧 Extend the Project

- **Add more gestures** → Detect multiple fingers, make complex gestures (e.g., "peace sign").  
- **Control different hardware** → LEDs, motors, relays instead of just servo.  
- **Improve communication** → Send structured data (like JSON) instead of plain strings.  
- **Integrate with Robotics** → Use the same setup for robot arms, cars, or drones.

---

## 📖 References

- [MediaPipe Hands Documentation](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)  
- [PySerial Documentation](https://pyserial.readthedocs.io/en/latest/)  
- [OpenCV Python Docs](https://docs.opencv.org/master/)  

---

👉 This project is a **foundation** for gesture-controlled robotics.  
From here, you can build **gesture-controlled robotic arms, cars, or even drones** 🚀
