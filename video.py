import cv2
import cv2.cv as cv
import os
import subprocess

pwd = '/home/sumukhshiv/Desktop/opencv_video'
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
    f = '0006'
    
    directory = pwd + '/output/' + f
    if not os.path.exists(directory):
        os.makedirs(directory)
    cv2.imwrite(directory +'/'+str(c).zfill(4) + '.jpg',frame)

    out = open("output.txt", "a")
    out2 = open("video_properties.txt", "a")
    time = vc.get(cv.CV_CAP_PROP_POS_MSEC)
    total_frames = vc.get(cv.CV_CAP_PROP_FRAME_COUNT)
    frame_rate = vc.get(cv.CV_CAP_PROP_FPS)
    length = (round(total_frames/frame_rate, 2))
    out.write(str(c).zfill(4) + " " + str(time) + "\n")
    
    
    c = c + 1
    total += 1
    cv2.waitKey(1)


out2.write('0006' + " " + str(total_frames) + ' ' + str(length) + "\n")
vc.release()
