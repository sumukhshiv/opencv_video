import cv2
import cv2.cv as cv


vc = cv2.VideoCapture('0006.mp4')
c=1
total = 0
fo = open('output.txt', 'w').close()
fo = open('video_properties.txt', 'w').close()

if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False

while rval:
    rval, frame = vc.read()
    cv2.imwrite(str(c).zfill(4) + '.jpg',frame)

    out = open("output.txt", "a")
    out2 = open("video_properties.txt", "a")
    time = vc.get(cv.CV_CAP_PROP_POS_MSEC)
    total_frames = vc.get(cv.CV_CAP_PROP_FRAME_COUNT)
    out.write(str(c).zfill(4) + " " + str(time) + "\n")
    out2.write('name' + " " + str(total_frames) + "\n")
    
    c = c + 1
    total += 1
    cv2.waitKey(1)
vc.release()
