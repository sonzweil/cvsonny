import cv2
import hand_solution
import math
import time
from mediapipe.python.solutions.hands import HandLandmark

cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()
    image = cv2.flip(image, 1)
    hp = hand_solution.HandProcessing()
    my_hands = hp.process_hands(image)

    if len(my_hands) != 0:
        for hand in my_hands:
            _, x1, y1 = hand.get_selected_landmark(HandLandmark.THUMB_TIP)
            _, x2, y2 = hand.get_selected_landmark(HandLandmark.PINKY_TIP)
            length = math.hypot(x2 - x1, y2 - y1)
            print(length)
    W = 8.5
    w = 110
    d = 50
    f = 650
    d = W*f/w
    time.sleep(0.01)
