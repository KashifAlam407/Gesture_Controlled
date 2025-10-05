### This is the python code for hand landmark detection and send data according to tip and pip difference to arduino through serial

import cv2
import mediapipe as mp
import serial
import time

# Initialize serial for Arduino
arduino = serial.Serial('COM12', 115200, timeout=1)  ## here select your "COM" port and baudrate, check your arduino IDE
time.sleep(2)

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    finger_status = []  # 1=open, 0=closed

    if results.multi_hand_landmarks:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            hand_label = hand_handedness.classification[0].label

            # thumb
            if hand_label == "Right":
                thumb_open = 1 if landmarks[4].x < landmarks[3].x else 0
            else:
                thumb_open = 1 if landmarks[4].x > landmarks[3].x else 0
            finger_status.append(thumb_open)

            # other fingers
            tips = [8, 12, 16, 20]
            pips = [6, 10, 14, 18]

            for tip, pip in zip(tips, pips):
                if landmarks[tip].y < landmarks[pip].y:
                    finger_status.append(1)  # Open
                else:
                    finger_status.append(0)  # Closed

            print("Finger Status [Thumb, Index, Middle, Ring, Pinky]:", finger_status)

            # Send to Arduino
            data = ''.join(map(str, finger_status))  # eg:- "01100"
            arduino.write((data + '\n').encode())

    cv2.imshow("Finger Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
