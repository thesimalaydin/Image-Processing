import cv2
import pyttsx3
import threading

engine = pyttsx3.init()

def speak_color(color):
    engine.say(f"Perceived color: {color}")
    engine.runAndWait()

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
speaking = False

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 15:
        color = "ORANGE"
    elif hue_value < 25:
        color = "ORANGE"
    elif hue_value < 35:
        color = "YELLOW"
    elif hue_value < 50:
        color = "YELLOW"
    elif hue_value < 60:
        color = "YELLOW"
    elif hue_value < 75:
        color = "GREEN"
    elif hue_value < 100:
        color = "GREEN"
    elif hue_value < 130:
        color = "BLUE"
    elif hue_value < 200:
        color = "VIOLET"
    elif hue_value < 215:
        color = "MAGENTA"
    elif hue_value < 240:
        color = "PURPLE"
    elif hue_value < 280:
        color = "ROSE"
    elif hue_value < 300:
        color = "PINK"
    else:
        color = "RED"


    if speaking:
        threading.Thread(target=speak_color, args=(color,)).start()
        speaking = False
    

    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)

    if key == ord(' '):  
        speaking = True

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()