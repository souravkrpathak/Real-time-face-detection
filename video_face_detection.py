import cv2
import time


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

a=1
while True:
	a = a+1
	check, frame = video.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#coordinates
	faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors=5)
	for xf,yf,wf,hf in faces:
		frame = cv2.rectangle(frame, (xf,yf), (xf+wf, yf+hf), (0,255,0), 3)
	cv2.imshow("Capturing (press \'q\' to quit)", frame)
	key = cv2.waitKey(1)
	
	if key == ord('q'):
		break

print(a) #number of frames


video.release()
cv2.destroyAllWindows()