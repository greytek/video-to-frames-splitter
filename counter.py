import cv2

cap = cv2.VideoCapture("test.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)  # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count / fps

# print('fps = ' + str(fps))
print('number of frames = ' + str(frame_count))
print('duration (S) = ' + str(duration))
minutes = int(duration / 60)
seconds = duration % 60
print('duration (M:S) = ' + str(minutes) + ':' + str(seconds))
total_time = minutes * 60 + seconds
print(total_time)
num = int(total_time)
interval = int((num / 5) )
print(interval)
increment = 0
f = open("Live Video Splitter/times.txt", "w")
for x in range(interval):
    increment = str(increment)
    f.write(increment)
    f.write("-")
    increment = int(increment)+5
    increment = str(increment)
    f.write(increment)
    f.write("\n")

f.close()

cap.release()
