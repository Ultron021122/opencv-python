import cv2
import numpy as np

captura = cv2.VideoCapture(0)
salida = cv2.VideoWriter('videoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))

bgr = [200, 200, 200]
thresh = 55
minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])

img = cv2.imread('rusia.jpg')
cielo = cv2.resize(img, (640,480),interpolation = cv2.INTER_NEAREST)

while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:
    frame = cv2.resize(imagen,(640,480),interpolation = cv2.INTER_AREA)
    fondo = np.uint8(bgr)
    maskBGR = cv2.inRange(frame, minBGR, maxBGR)
    mask_inv = cv2.bitwise_not(maskBGR)

    resultBGR = cv2.bitwise_and(frame, frame, mask = mask_inv)
    result_inv = cv2.bitwise_and(cielo, cielo, mask = maskBGR)

    total = cv2.add(resultBGR, result_inv)
    cv2.imshow('resultado total',total)
    salida.write(total)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
captura.release()
salida.release()
cv2.destroyAllWindows()
