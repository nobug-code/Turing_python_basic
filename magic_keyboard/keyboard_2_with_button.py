import cv2
from cvzone.HandTrackingModule import HandDetector
# 카메라를 VideoCapture 객체로 가져온다.
cap = cv2.VideoCapture(0)

# Minimum Detection Confidence Threshold
detector = HandDetector(detectionCon=0.8)
colorR = (255, 0, 255)

class Button():

    def __init__(self, pos, text, size=[100, 100]):
        self.pos = pos
        self.text = text
        self.size = size




    def draw_box(self, img):
        x, y = self.pos
        w, h = self.size

        # 그냥 상자 그리기
        cv2.rectangle(img, self.pos, (x + w, y + h), colorR, cv2.FILLED)
        # 글 그려서 넣깅 , 4번째는 font scale
        cv2.putText(img, self.text, (x + 10, y + 10),
        cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
        return img


mybuton = Button([100, 100], "Q")


while True:
    # 계속해서 이미지를 불러와서 영상을 보여준다.
    success, img = cap.read()
    # Find the hand and its landmarks
    # 이미지 좌우 반전
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)  # with draw

    # 그림 거려
    img = mybuton.draw_box(img)

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right
        fingers1 = detector.fingersUp(hand1)

        l, _, _ = detector.findDistance(lmList1[8], lmList1[12], img)



    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
