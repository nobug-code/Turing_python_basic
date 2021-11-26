'''
가우시안 블러링

가우시안 분포를 갖는 커널로 블러링을 하는 것.

가우시안 분포가 뭔데 ? 정규분포라고도 한다. 값이 평균 근처에 많고 평균에서 멀어질수록 개수가 작아진다.

블러링 커널에서 가우시안은

중앙값이 가장 크고, 중앙에서 멀어질 수록 그 값이 작아지는 것을 뜻한다.

'''
'''
1, 2, 1
2, 4, 2  x 1/16
1, 2, 1

16으로 나눈 이유는 커널의 모든 요소의 합이 16이기 때문이다. 

그럼 왜써? 대상 픽셀에 가가울수록 영향을 주고, 멀어질수록 적은 영향을 주기 때문에 원래의 영상과 비슷하면서
노이즈를 제거하는 효과가 있다. 
'''
import cv2

img = cv2.imread("./imgs/circle.png")
# 커널을 생성하지 않고 적용
# img, 커널 크기, 0 이면 표준편차 적용
blur = cv2.GaussianBlur(img, (3, 3), 0)



cv2.imshow('gaussian blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()