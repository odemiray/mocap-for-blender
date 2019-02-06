# USAGE
# python video_facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat
# python video_facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --picamera 1

# import the necessary packages
from imutils.video import VideoStream
from imutils import face_utils
import datetime
import imutils
import time
import dlib
import cv2 as cv
 
predictorpath = "shape_predictor_68_face_landmarks.dat"
# construct the argument parse and parse the arguments 
# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictorpath)

# initialize the video stream and allow the cammera sensor to warmup
print("[INFO] camera sensor warming up...")
#vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

cam = cv.VideoCapture(0)

# loop over the frames from the video stream
while True:
        # grab the frame from the threaded video stream, resize it to
    # have a maximum width of 400 pixels, and convert it to
    # grayscale
    retl_val, frame = cam.read()
    frame = cv.resize(frame, None, fx=0.3, fy=0.3)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # detect faces in the grayscale frame
    rects = detector(gray, 0)

    # loop over the face detections
    for rect in rects:
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # loop over the (x, y)-coordinates for the facial landmarks
        # and draw them on the image
        for (x, y) in shape:
            cv.circle(frame, (x, y), 1, (0, 0, 255), -1)
      
    # show the frame
    frame = cv.resize(frame, None, fx= 4, fy = 4)
    cv.imshow("Frame", frame)
    key = cv.waitKey(1) & 0xFF
 
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
 
# do a bit of cleanup
cv.destroyAllWindows()
cam.release()
