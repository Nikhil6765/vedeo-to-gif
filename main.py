from moviepy.editor import *

video=VideoFileClip('videoplayback.mp4')

video.write_gif('videoplayback.gif')