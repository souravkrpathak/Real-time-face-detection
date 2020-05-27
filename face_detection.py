import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")


img = cv2.imread("culfest.JPG")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#coordinates
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.3, minNeighbors=5)
smile = smile_cascade.detectMultiScale(gray_img, scaleFactor = 1.9, minNeighbors=20)
# print(faces)

for xf,yf,wf,hf in faces:
	img = cv2.rectangle(img, (xf,yf), (xf+wf, yf+hf), (0,0,255), 3)

for xs,ys,ws,hs in smile:
	img = cv2.rectangle(img, (xs,ys), (xs+ws, ys+hs), (0,255,0), 3)

resized = cv2.resize(img, (640,820))
cv2.imshow("gray", resized)
cv2.waitKey(10000)
# cv2.destroyAllWindows()