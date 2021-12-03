import cv2
from cvzone.HandTrackingModule import HandDetector
# 카메라를 VideoCapture 객체로 가져온다.
cap = cv2.VideoCapture(0)

# Minimum Detection Confidence Threshold
detector = HandDetector(detectionCon=0.8)

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", "." ,"/"]]


colorR = (255, 0, 255)

class Button():

    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.text = text
        self.size = size



# list로 만들어줘
buttonList = []
for out_num, key in enumerate(keys):
    for num, key_elm in enumerate(key):
        buttonList.append(Button([100 * num + 50, 100 * out_num + 50], key_elm))

def drawALL(img, buttonList):

    for button in buttonList:

        x, y = button.pos
        w, h = button.size
        # 그냥 상자 그리기
        cv2.rectangle(img, button.pos, (x + w, y + h), colorR, cv2.FILLED)
        # 글 그려서 넣깅 , 4번째는 font scale, 칼러 다음에는 두께
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

    return img
while True:
    # 계속해서 이미지를 불러와서 영상을 보여준다.
    success, img = cap.read()
    # Find the hand and its landmarks
    # 이미지 좌우 반전
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)  # with draw
    img = drawALL(img, buttonList)
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right
        fingers1 = detector.fingersUp(hand1)


        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            print(lmList1[8][0], w, w)
            if x < lmList1[8][0] < x + w and y < lmList1[8][1] < y + h:
                print("hi")
                cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                # 글 그려서 넣깅 , 4번째는 font scale, 칼러 다음에는 두께
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

                l, _, _ = detector.findDistance(lmList1[8], lmList1[12], img)

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
