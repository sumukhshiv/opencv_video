import os
import cv2
import cv2.cv as cv

def analyze(skip_number):

    rootdir = '/home/sumukhshiv/Desktop/test'

    for files in os.walk(rootdir):
        # print files[2:][0][:-1]
        for f in files[2:][0][:-1]:
            # print f
            c=1
            total = 0
            f_name = f[:-4]
            f_text = 'txt_' + f_name
            directory = rootdir + '/output/' + f_name
            if not os.path.exists(directory):
                os.makedirs(directory)
            fo = open(directory + '/' + f_text + '.txt', 'w').close()
            vc = cv2.VideoCapture(f)
            if vc.isOpened():
                rval , frame = vc.read()
            else:
                rval = False

            while rval:
                rval, frame = vc.read()
                if skip_number == 0:
                    cv2.imwrite(directory +'/'+str(c).zfill(4) + '.jpg',frame)

                elif (skip_number != 0) and (c % skip_number == 1):
                    cv2.imwrite(directory +'/'+str(c).zfill(4) + '.jpg', frame)

                time = vc.get(cv.CV_CAP_PROP_POS_MSEC)
                total_frames = vc.get(cv.CV_CAP_PROP_FRAME_COUNT)
                frame_rate = vc.get(cv.CV_CAP_PROP_FPS)
                length = (round(total_frames/frame_rate, 2))
                out = open(directory + '/' + f_text + '.txt', "a")
                out.write(str(c).zfill(4) + " " + str(time) + "\n")


                c = c + 1
                total += 1
                cv2.waitKey(1)
            fo = open('output/video_properties.txt', 'w').close()
            out2 = open("output/video_properties.txt", "a")
            out2.write(f + " " + str(total_frames) + ' ' + str(length) + "\n")

    vc.release()

analyze(2)
