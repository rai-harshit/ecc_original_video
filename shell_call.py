import subprocess
subprocess.call(['./extract.sh']) 
print("Shell-Script executed successfully")


# import subprocess as sp
# command = [ 'ffmpeg',
#             '-i', 'a.mp4',
#             '-f', 'image2pipe',
#             '-pix_fmt', 'rgb24',
#             '-vcodec', 'rawvideo', '-']
# pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)
# pipe.
