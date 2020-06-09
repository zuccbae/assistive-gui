REFERENCES FOR THE CODE:
    https://pysource.com/category/tutorials/gaze-controlled-keyboard/
    https://towardsdatascience.com/mouse-control-facial-movements-hci-app-c16b0494a971#:~:text=Mouse%20Cursor%20Control%20Using%20Facial%20Movements%20%E2%80%94%20An%20HCI%20Application,-Akshay%20L%20Chandra&text=This%20HCI%20(Human%2DComputer%20Interaction,wearable%20hardware%20or%20sensors%20needed.

import cv2
import numpy as np
import dlib
from math import hypot
import pyautogui as pag


## failsafe

pag.FAILSAFE = False

##xy pair determined by resultoinon screen
##obtain coordinates of mouse on computer screen

# This launches the camera, 0 is the position of my first camera any other additional cameras are listed 1,
# 2, 3, etc, etc.
cap = cv2.VideoCapture(0)

# this is a pre-trained data set, this is for the facial landmarks of any face, it has a total of 68 pre-recognised
# points in a face
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# my first function, this is for finding the midpoint of two points, this useful when finding the absolute center of the
# eye


def midpoint(p1, p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)
    return midpoint()

# the font that is displayed is clear enough to be properly seen
font = cv2.FONT_HERSHEY_TRIPLEX

def ratio(points, f_landmarks):
    left_point = (f_landmarks.part(points[0]).x, f_landmarks.part(points[0]).y)
    right_point = (f_landmarks.part(points[3]).x, f_landmarks.part(points[3]).y)
    center_top = midpoint(f_landmarks.part(points[1]), f_landmarks.part(points[2]))
    center_bottom = midpoint(f_landmarks.part(points[5]), f_landmarks.part(points[4]))

    # hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 1)
    # ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 1)

    hor_line_length = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_length = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    blink = hor_line_length / ver_line_length

    return blink


def get_gaze_ratio(points, f_landmarks):
    region_left = np.array([(f_landmarks.part(points[0]).x, f_landmarks.part(points[0]).y),
                            (f_landmarks.part(points[1]).x, f_landmarks.part(points[1]).y),
                            (f_landmarks.part(points[2]).x, f_landmarks.part(points[2]).y),
                            (f_landmarks.part(points[3]).x, f_landmarks.part(points[3]).y),
                            (f_landmarks.part(points[4]).x, f_landmarks.part(points[4]).y),
                            (f_landmarks.part(points[5]).x, f_landmarks.part(points[5]).y)], np.int32)

    height, width, _ = frame.shape
    mask = np.zeros((height, width), np.uint8)

    cv2.polylines(mask, [region_left], True, (255, 255, 255), 1)
    cv2.fillPoly(mask, [region_left], 255)

# shows eye in the mask to eye-solate it
    eye = cv2.bitwise_and(gray, gray, mask=mask)
    # cv2.imshow("eye", eye)

    min_x = np.min(region_left[:, 0])
    max_x = np.max(region_left[:, 0])
    min_y = np.min(region_left[:, 1])
    max_y = np.max(region_left[:, 1])

    gray_eye = eye[min_y: max_y, min_x: max_x]
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY_INV)
    threshold_eye = cv2.resize(threshold_eye, None, fx=5, fy=5)
    cv2.imshow("T", threshold_eye)

    masked_eye = cv2.resize(gray_eye, None, fx=5, fy=5)

    cv2.imshow("Masked Eye", masked_eye)

    height, width = threshold_eye.shape
    left_thresh = threshold_eye[0: height, 0: int(width / 2)]
    left_thresh_black = cv2.countNonZero(left_thresh)

    right_thresh = threshold_eye[0: height, 0: int(width / 2): width]
    right_thresh_black = cv2.countNonZero(right_thresh)

    if left_thresh_black == 0:
        determination = 1
    elif right_thresh_black == 0:
        determination = 10
    else:
        determination = left_thresh_black / right_thresh_black

    return determination


while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 255), 2)

        landmarks = predictor(gray, face)

        # Blink Detection Ratio

        if landmarks != predictor(gray, face):
            cv2.putText(frame, "Face Detection Ready.", (400, 400), font, 0.5, (0, 0, 255), 0)
        else:
            cv2.putText(frame, "Face NOT Detected, Please Come Into The Frame", (0, 100), font, 0.5, (0, 0, 255), 0)
# BLINK
        ler = ratio([36, 37, 38, 39, 40, 41], landmarks)
        rer = ratio([42, 43, 44, 45, 46, 47], landmarks)
        b_ratio = ((ler + rer)/2)

        if b_ratio > 5:
            cv2.putText(frame, "Blink Detected", (0, 100), font, 0.5, (0, 0, 255), 0)
            pag.click() ##left click
            pag.click(clicks=2, interval=0.225)##doubleclick
            pag.scroll(-60, x=200, y=420)

        # Gaze Detection

        gaze_ratio_left = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks)
        gaze_ratio_right = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks)

        determination = ((gaze_ratio_left + gaze_ratio_right)/2)

        if determination < 72:
            cv2.putText(frame, "Left", (200, 100), font, 2, (0, 0, 255), 2)
            pag.moveTo(200, 420, duration=0.2)
        elif 73 < determination < 85:
            cv2.putText(frame, "Right", (200, 100), font, 2, (0, 0, 255), 2)
            pag.moveTo(1600, 420, duration=0.2)
        elif determination >= 86:
            cv2.putText(frame, "Center", (200, 100), font, 2, (0, 0, 255), 2)
        else:
            cv2.putText(frame, "Undetected", (200, 100), font, 2, (0, 0, 255), 2)

        cv2.putText(frame, str(determination), (300, 100), font, 2, (126, 221, 106), 2)

    cv2.imshow("Front Camera", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
