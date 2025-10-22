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

background = np.full((400, 400, 3), (180, 255, 180), dtype=np.uint8)
bitwise_or = cv2.bitwise_or(canvas, background)
cv2.imwrite("output/bitwise_or.png", bitwise_or)