import numpy as np
import cv2, sys


def OpenVideo ( index = cv2.CAP_DSHOW ):
	cap = cv2.VideoCapture(index)
	ret, frame = cap.read()

	if ret == False:
		OpenVideo(index+1)
	elif cap.isOpened() == False:
		cap.open(index)
	return cap, ret, frame



cap, ret, frame = OpenVideo()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()