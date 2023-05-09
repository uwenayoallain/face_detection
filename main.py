import cv2
import time
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
counter = 0
limit = 10
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 2)
        sub_face = img[y:y+h, x:x+w]
        FaceFileName = "faces/face_" + str(y) + ".jpg"
        cv2.imwrite(FaceFileName, sub_face)
        counter += 1
        time.sleep(0.01) # pause for 0.01 seconds
    cv2.imshow('img',img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()