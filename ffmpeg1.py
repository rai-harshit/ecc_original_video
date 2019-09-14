from subprocess import check_output
import os, time
import subprocess

s_t = time.time()

# inp = "test.mp4"
# out = "out.mp4"

# os.system("ffmpeg -i {} -vf \"boxblur=150:1\" -codec:a copy {}".format(inp,out))
# os.system("ffmpeg -i test1.mp4 -vf \"boxblur=150:1,boxblur=enable='between(t,5,15)'\" -codec:a copy output.avi")
os.system("ffmpeg -i test.mp4 -filter_complex \"boxblur=90:enable='if(between(t,3,10)+between(t,15,20)+between(t,23,28),1,0)\" -codec:a copy test.avi | vlc test.avi")
# os.system("rm -rf test2.avi")
# def get_pid(name):
# 	return int(check_output(["pidof",name]))

# def kill_proc(name):
	# x = int(check_output(["pidof",name]))
	# ids = get_pid("ffmpeg")
	# print("Killed Process: {}".format(x))
	# for id in ids:
	# os.system("kill -9 {}".format(ids))

# os.system("ffmpeg -i test2.mp4 -ss 00:00:00 -to 00:01:00 -codec:a copy test2.avi ") # | vlc test2.avi
# kill_proc("ffmpeg")
# os.system("rm ~/Desktop/test2.avi")

# os.system("ffmpeg -i test2.mp4 -ss 00:01:00 -to 00:02:00 -codec:a copy test2.avi | vlc test2.avi")
# kill_proc()
# os.system("rm ~/Desktop/test2.avi")

# def getLength(input_video):
# result = subprocess.Popen('ffprobe -i test211.mp4 -show_entries format=duration -v quiet -of csv="p=0"', stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
# output = result.communicate()
# print(output[0])

# # getLength("test211.mp4")

# e_t = time.time()
# t_t = e_t - s_t

# print("Total time: {}".format((t_t)))
