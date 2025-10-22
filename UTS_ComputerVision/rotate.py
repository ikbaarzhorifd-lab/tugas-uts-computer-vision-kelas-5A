import cv2
import numpy as np
import os

os.makedirs("output", exist_ok=True)

canvas = np.full((400, 400, 3), 255, dtype=np.uint8)

cv2.rectangle(canvas, (140, 80), (260, 160), (180, 180, 180), -1)
cv2.circle(canvas, (170, 120), 10, (0, 0, 0), -1)
cv2.circle(canvas, (230, 120), 10, (0, 0, 0), -1)
cv2.line(canvas, (170, 145), (230, 145), (0, 0, 0), 2)
cv2.rectangle(canvas, (150, 160), (250, 300), (200, 200, 200), -1)
cv2.line(canvas, (150, 180), (100, 240), (0, 0, 0), 5)
cv2.line(canvas, (250, 180), (300, 240), (0, 0, 0), 5)
cv2.line(canvas, (200, 80), (200, 50), (0, 0, 0), 3)
cv2.circle(canvas, (200, 45), 5, (0, 0, 255), -1)

cv2.imwrite("output/karakter.png", canvas)

M_rotate = cv2.getRotationMatrix2D((200, 200), 30, 1)
rotated = cv2.warpAffine(canvas, M_rotate, (400, 400))
cv2.imwrite("output/rotate.png", rotated)
