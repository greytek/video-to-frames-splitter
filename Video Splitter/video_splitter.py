from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import cv2


def counter(required_video_file):
    cap = cv2.VideoCapture(required_video_file)
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
    interval = int((num / 5))
    print(interval)
    increment = 0
    f = open("videoTimes.txt", "w")
    for x in range(interval):
        increment = str(increment)
        f.write(increment)
        f.write("-")
        increment = int(increment) + 5
        increment = str(increment)
        f.write(increment)
        f.write("\n")
    f.close()
    cap.release()


def slicing(required_video_file):
    with open("videoTimes.txt") as f:
        times = f.readlines()

    times = [x.strip() for x in times]

    for time in times:
        start_time = int(time.split("-")[0])
        end_time = int(time.split("-")[1])
        ffmpeg_extract_subclip(required_video_file, start_time, end_time,
                               targetname=str(times.index(time) + 1) + ".mp4")


required_video_file = "test.mp4"
counter(required_video_file)
slicing(required_video_file)
