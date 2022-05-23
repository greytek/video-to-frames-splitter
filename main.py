import ffmpeg
import sys

sys.path.append(r'C:\Program Files\ffmpeg-n4.4-latest-win64-gpl-4.4\bin')

stream = ffmpeg.input('Video Splitter/test.mp4')
stream = stream.trim(start=10, duration=15).filter('setpts', 'PTS-STARTPTS')
stream = stream.filter('fps', fps=5, round='up').filter('scale', w=128, h=128)
stream = ffmpeg.output(stream, 'output.mp4')
ffmpeg.run(stream)
