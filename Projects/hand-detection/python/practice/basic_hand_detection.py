import cv2
import mediapipe as mp

## 1. Create short names for mediapipe modules
mp_hands = mp.solutions.hands  ## Hands module
mp_drawing = mp.solutions.drawing_utils  ## Drawing helper

## 2. Create an object of Hands class
hands = mp.solutions.hands.Hands(
    static_image_mode=False,  ## Video = Fasle, Image = True
    max_num_hands=1,  ## Detect up to 2 hands
    min_detection_confidence=0.5,  ## Minimum confidence for detection
    min_tracking_confidence=0.5  ## Minimum confidence for tracking
)

## 3. Start Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  ## The boolean ret is True if the frame was successfully read, and the frame element is the actual image data captured
    if not ret:
        break

    ## 4. Convert to RGB (Mediapipe needs RGB, OpenCv gives BGR)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    ## 5. Call process() method on hands object
    results = hands.process(frame_rgb)

    ## 6. Check results --> attributes of results
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # drawing_spec = mp.solutions.drawing_utils.DrawingSpec(color=(0,0,255), thickness=3, circle_radius=4)   ### landmark_drawing_spec=drawing_spec,connection_drawing_spec=drawing_spec --- add these two to mp_drawing.draw_landmarks(..)

            ## Draw landmarks
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )

            ## Access attributes of each landmarks
            # for id, lm in enumerate(hand_landmarks.landmark):
            #     print(f"Landmark {id}: x={lm.x}, y={lm.y}, z={lm.z}")

            
            print(hand_landmarks.landmark[4].z)  # Thumb tip X

    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()