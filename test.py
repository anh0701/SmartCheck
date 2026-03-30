from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train/weights/best.pt")


results = model("dataset/valid/images/diote.jpg", show=True)


img = results[0].plot()

cv2.imshow("Result", img)
cv2.waitKey(0)   
cv2.destroyAllWindows()