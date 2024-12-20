#This code demonstrate how to show location of hand landmark
import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw 
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

img = cv2.imread('shape.png')
fontpath = "./angsana.ttc" 
font = ImageFont.truetype(fontpath, 30)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 7:
                    id7 = int(id)
                    cy7 = cy
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 11:
                    id11 = int(id)
                    cy11 = cy
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 15:
                    id15 = int(id)
                    cy15 = cy
                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 19:
                    id19 = int(id)
                    cy19 = cy
            img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(img_pil)
            if cx4 < cx3:
                draw.text((280, 300), "โป้ง", font=font, fill=(44, 126, 214))
            if cy8 < cy7:
                draw.text((280, 330), "ชี้", font=font, fill=(175, 54, 60))
            if cy12 < cy11:
                draw.text((280, 360), "กลาง", font=font, fill=(157, 188, 64))
            if cy16 < cy15:
                draw.text((280, 390), "นาง", font=font, fill=(187, 86, 149))
            if cy20 < cy19:
                draw.text((280, 420), "ก้อย", font=font, fill=(8, 133, 161))//เปลี่ยนโค๊ดสีด้วย
        draw.text((450, 8), "นายภูมิ เหลี่ยมวานิช", font=font, fill = (0,255,255)) // ใส่ชื่อมีง
        draw.text((510, 38), "670610774", font=font, fill = (0,255,255))//เลขมึง
        img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()