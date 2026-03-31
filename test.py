from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train/weights/best.pt")


results = model("dataset/test/images/capacitors-2-_jpg.rf.0385cd49a870faa91ece9498ec91e825.jpg", show=True)


img = results[0].plot()

cv2.imshow("Result", img)
cv2.waitKey(0)   
cv2.destroyAllWindows()