import cv2
import mediapipe as mp
import pyautogui

# Setup PyAutoGUI
pyautogui.PAUSE = 0.1
# Leave FAILSAFE enabled to allow manual interruption by corner move :contentReference[oaicite:1]{index=1}

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Camera setup
cam = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

if not cam.isOpened():
    print("Error: Could not open camera.")
    cam.release()
    exit()

while True:
    ret, frame = cam.read()
    if not ret:
        print("Error: Failed to read camera.")
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        # Skip motion/grabs if no face is found
        print("No face landmarks detected")
    else:
        lm = results.multi_face_landmarks[0].landmark

        # Track iris landmarks 474–477
        for idx, i in enumerate([474, 475, 476, 477]):
            x = int(lm[i].x * w)
            y = int(lm[i].y * h)
            cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)

            if idx == 1:
                mouse_x = int(lm[i].x * screen_w)
                mouse_y = int(lm[i].y * screen_h)

                if pyautogui.onScreen(mouse_x, mouse_y):
                    try:
                        pyautogui.moveTo(mouse_x, mouse_y)
                    except pyautogui.FailSafeException:
                        print("⚠️ Emergency stop: mouse hit corner")
                        cam.release()
                        cv2.destroyAllWindows()
                        face_mesh.close()
                        exit()

        # Blink detection with landmarks 145 (upper) & 159 (lower)
        top = lm[145]
        bottom = lm[159]
        if (top.y - bottom.y) < 0.01:
            try:
                pyautogui.click()
                pyautogui.sleep(1)
                print("Mouse clicked")
            except pyautogui.FailSafeException:
                print("⚠️ Emergency stop on click")
                cam.release()
                cv2.destroyAllWindows()
                face_mesh.close()
                exit()

    cv2.imshow("Eye Controlled Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cam.release()
cv2.destroyAllWindows()
face_mesh.close()
