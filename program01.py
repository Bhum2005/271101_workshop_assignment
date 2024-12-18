#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Nfing = 0
cap = cv2.VideoCapture(0)
pong=0
cee=0
klang=0
nang=0
koi=0
#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

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
            if cx4 > cx3:
                pong = 0
            else:
                pong = 1
            if cy8>cy7:
                cee = 0
            else:
                cee = 1
            if cy12>cy11:
                klang = 0
            else:
                klang = 1
            if cy16>cy15:
                nang = 0
            else:
                nang = 1
            if cy20>cy19:
                koi = 0
            else:
                koi = 1
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    Nfing = pong+cee+klang+nang+koi
    cv2.putText(img, str(int(Nfing)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()