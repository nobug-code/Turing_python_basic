'''
필터와 컨볼루션

공간 영역 필터링은 연산 대상 픽셀과 그 주변 픽셀들을 활용하여 새로운 픽셀 값을 얻는것.
이러한 작업을 수행하는게 커널

(그림으로 설명)

커널 == window == fileter == mask
'''

# 평균 블러링
'''
영상을 흐릿하게 하는 작업. 마치 초첨이 맞지 않게 사물을 바라 보는것과 비슷하다. 
가장 간단한 방법은 평균 블러링이 있다. 주변 픽셉 값들의 평균을 적용한다.
'''

import cv2
import numpy as np

# 이미지 불러오기
img = cv2.imread("imgs/test.jpg")

# 커널 생성
kernel = np.ones((5,5))/5**2 # 커널을 그려보아라

# filter2d는 연산을 해주는거
# src : img 를 넣어준다.
# ddepth : 출력영상의 dtype(-1: 입력영상과 동일)
# kernel : 컨볼루션 커널, float32의 n xn 크기 배열
blured = cv2.filter2D(img, -1, kernel)

# 결과 출력
cv2.imshow("original", img)
cv2.imshow("blur", blured)
cv2.waitKey()
cv2.destroyAllWindows()

# 커널 사이즈랑 값을 변경시켜서 확인해봐라
