#opencv(computer vision)

import cv2
print(cv2.__version__)

img1 = cv2.imread('panda.jpeg')
print(type(img1))

cv2.imshow('image test', img1)
cv2.waitKey()
cv2.destroyAllWindows()

print('end')

#다른 이름으로 저장
cv2.imwrite('panda2.jpeg', img1)
cv2.imwrite('panda3.jpeg', img1, [cv2.IMWRITE_JPEG_QUALITY, 10]) #quality 낮음 -> 메모리 덜 씀

#이미지 크기 조정
img2 = cv2.resize(img1, (300, 100), interpolation=cv2.INTER_AREA)
cv2.imwrite('panda3.jpeg', img2)
#이미지 밝기 조정
#이미지 상하좌우 회전
#특정 영역 자르기