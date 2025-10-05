# Gesture Controlled Projects (MediaPipe + Arduino)

This repository contains **gesture-controlled robotics projects** built with **MediaPipe, OpenCV, Python, and Arduino**.  
It serves both as a **learning reference** (documentation, trees, explanations) and as a **project collection** (hand, thumb, face, eye detection).

---

## 📂 Repository Structure

```
gesture-control/
│
├── docs/                    
│   ├──      
│   ├──       
│   ├── 
│   ├── images/
│   │   ├── mediapipe_hand_tree.png
│   │   ├── landmarks_example.png
│   │   └── opencv_flow.png
│   └── diagrams/
│       └── python-arduino-flow.png
│
├── projects/                 
│   ├── hand-detection/
│   ├── thumb-detection/
│   ├── face-detection/
│   └── eye-detection/
│
├── LICENSE
└── README.md                
```

---

# 🌳 MediaPipe Solutions – Master Tree

```
mediapipe.solutions
│
├── hands                     # Hand landmark detection (21 keypoints)
│   ├── Hands (class) → process(image) → results
│   └── hands_connections
│
├── drawing_utils              # Draw landmarks, connections
├── drawing_styles             # Predefined drawing styles
│
├── face_detection             # Face bounding box & keypoints
├── face_mesh                  # Dense 468-point face mesh
│   └── face_mesh_connections
│
├── pose                       # Full body pose detection (33 keypoints)
│   └── pose_connections
│
├── holistic                   # Combined face, hands, pose
│
├── objectron                  # 3D object detection (shoes, cups, etc.)
│
├── selfie_segmentation        # Segment person from background
│
└── download_utils             # Model downloading helpers
```

---

## 🌳 Hands Module

```
mediapipe.solutions.hands
   └── Hands (class)
         ├── __init__(...)           
         └── process(image)           
                ↓
             results (object)
                ├── multi_hand_landmarks              # 21 keypoints per hand
                ├── multi_handedness                  # Left / Right hand
                └── multi_hand_world_landmarks        # 3D world coordinates
```

👉 Use for real-time **hand gesture recognition**, finger tracking, robotic control.

---

## 🌳 Drawing Utilities

```
mediapipe.solutions.drawing_utils
   ├── draw_landmarks(image, landmark_list, connections, …)
   ├── DrawingSpec (class)
   ├── plot_landmarks(landmark_list, connections, …)
   └── Predefined Connections
```

👉 For **visualizing landmarks & connections** on images/frames.

---

## 🌳 Drawing Styles

```
mediapipe.solutions.drawing_styles
   ├── get_default_hand_landmarks_style()
   ├── get_default_hand_connections_style()
   ├── get_default_pose_landmarks_style()
   └── get_default_face_mesh_style()
```

👉 Provides **ready-made color/thickness styles**.

---

## 🌳 Face Detection

```
mediapipe.solutions.face_detection
   └── FaceDetection (class)
         └── process(image) → results.detections
                ├── location_data.relative_bounding_box
                └── keypoints (e.g. eyes, nose tip)
```

👉 Use when you just need **face box/keypoints**, not full mesh.

---

## 🌳 Face Mesh

```
mediapipe.solutions.face_mesh
   └── FaceMesh (class)
         └── process(image) → results.multi_face_landmarks
                ├── 468 landmarks per face
                ├── face_mesh_connections
```

👉 For **AR, facial gestures, expressions**.

---

## 🌳 Pose

```
mediapipe.solutions.pose
   └── Pose (class)
         └── process(image) → results.pose_landmarks
                ├── 33 body landmarks
                └── pose_connections
```

👉 Detects **skeleton joints** for full-body gestures.

---

## 🌳 Holistic

```
mediapipe.solutions.holistic
   └── Holistic (class)
         └── process(image) → results
                ├── face_landmarks
                ├── left_hand_landmarks
                ├── right_hand_landmarks
                └── pose_landmarks
```

👉 Best for **whole-body multimodal gesture recognition**.

---

## 🌳 Objectron

```
mediapipe.solutions.objectron
   └── Objectron (class)
         └── process(image) → results.detected_objects
                ├── 3D bounding box (shoes, chairs, cups)
                └── keypoints in 3D
```

👉 For **3D object pose estimation**.

---

## 🌳 Selfie Segmentation

```
mediapipe.solutions.selfie_segmentation
   └── SelfieSegmentation (class)
         └── process(image) → results.segmentation_mask
```

👉 Separates **foreground (person)** from background.

---

## 🌳 Download Utils

```
mediapipe.solutions.download_utils
   ├── download_oss_model(model_name)
   └── ensure_model_downloaded()
```

👉 Handles **downloading models** on demand.

---

# 🖼️ Hand Landmarks Example

- **21 points per hand** (wrist, MCP, PIP, DIP, fingertip joints)  
- Coordinates: `x, y` (normalized), `z` (relative depth)

![Hand Landmarks](docs/images/landmarks_example.png)

---

# 🚦 How Projects Work

1. **Arduino**:  
   - Upload sketch (e.g. `serial_receiver.ino`)  
   - Arduino listens for serial commands and controls hardware  

2. **Python + MediaPipe**:  
   - Capture video (`cv2.VideoCapture`)  
   - Detect landmarks using `Hands.process()`  
   - Apply logic (e.g. check if finger up/down)  
   - Send commands over serial (`pyserial`)  

3. **Arduino Executes**:  
   - Receives command string (e.g. `"INDEX_UP"`)  
   - Maps to servo/LED/motor action  

---

# 🎯 Usage

### Install
```bash
pip install mediapipe opencv-python pyserial
```

### Run
1. Upload Arduino sketch  
2. Run Python detection code (`hand_detection_code.py`)  
3. Move hand in front of webcam  
4. Arduino reacts in real time 🎉

---

# 🔄 Extend Projects

- Add new gestures by checking landmark positions  
- Add Arduino actions (servos, motors, relays)  
- Use other solutions (`face_mesh`, `pose`, `objectron`) for advanced robotics  

---

# 📜 License & Contribution

Open source under MIT License.  
Contributions welcome: new projects, docs, improvements.

---
