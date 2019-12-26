import cv2
import time

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

custom_img = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        #scaleFactor – Parameter specifying how much the image size is reduced at each image scale.
        scaleFactor=1.1,
        #minNeighbors – Parameter specifying how many neighbors each candidate rectangle should have to retain it.
        minNeighbors=5,
        minSize=(30, 30),
    )


    cv2.putText(frame, 'Hellooo ', (100, 130), font, 1,(255, 255, 255), 2)

    print(type(faces))
    # Draw a rectangle around the faces
    # 좌표랑 그려주는 색깔을 지정
    for (x, y, w, h) in faces:
        print(x,y,w,h)
        #cv2.rectangle(frame, (x, y), (x+w, y+h),(0, 255, 0), 2)
        cv2.circle(frame, (x, y), 55, (0, 255, 0), 1)
        cv2.line(frame, (0,0), (100,100), (185, 128, 41), 2)
    time.sleep(0.1)

    # Display the resulting frame
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

#출저
# https://github.com/shantnu/Webcam-Face-Detect

'''
cascade – Haar classifier cascade (OpenCV 1.x API only). It can be loaded from XML or YAML file using Load(). When the cascade is not needed anymore, release it using cvReleaseHaarClassifierCascade(&cascade).
image – Matrix of the type CV_8U containing an image where objects are detected.
objects – Vector of rectangles where each rectangle contains the detected object.
scaleFactor – Parameter specifying how much the image size is reduced at each image scale.
minNeighbors – Parameter specifying how many neighbors each candidate rectangle should have to retain it.
flags – Parameter with the same meaning for an old cascade as in the function cvHaarDetectObjects. It is not used for a new cascade.
minSize – Minimum possible object size. Objects smaller than that are ignored.
maxSize – Maximum possible object size. Objects larger than that are ignored.
'''

틱택톡

def start_mark():

