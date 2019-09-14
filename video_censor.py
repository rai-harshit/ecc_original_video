import warnings
warnings.filterwarnings("ignore")
from keras.models import load_model
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import cv2
from tqdm import tqdm
import numpy as np
import time
import shutil
import keras.backend as K

import tensorflow as tf
from keras.backend.tensorflow_backend import set_session
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.25
set_session(tf.Session(config=config))


# rootd = "/home/g_host/Desktop/dtoxd/hr/ecc/"
model_file = ".\\model.h5"
frames_store = ".\\storage\\frames\\"
video = "test.mp4"
sensitivity = 0.05

ext_start = time.time()

os.system('ffmpeg -i {} -vf  "select=gt(scene\\,{}), scale=300:300, showinfo" -vsync vfr {}%01d.jpg 2>&1 | findstr /r "pts_time:[0-9]*.[0-9]*" > timestamp.log'.format(video,sensitivity,frames_store))
ext_end = time.time()

# print("Frame Extraction Completed Successfully")
frames = os.listdir(frames_store)
# frames.sort()
# print(frames)

list1 = []
for fms in frames:
	fms = int(fms.split(".")[0])
	list1.append(fms)
list1.sort(key=int)

# print(list1)

with open("timestamp.log") as f:
    data = f.read()
TsData = []
withoutNewLine = data.split("\n")
for line in withoutNewLine:
    if "pts_time:" in line:
        TsData.append(line.split("pts_time:")[1])
timestamps = []
for data in TsData:
    t = data.split(" ")[0]
    timestamps.append(t)

test_data = []
for frame in tqdm(list1):
	# print(frames_store+str(frame)+".jpg")
	im = cv2.imread(frames_store+str(frame)+".jpg")
	# print(im.shape)
	test_data.append(im)
test_data = np.array(test_data)
model = load_model(model_file)
result = []

predict_start = time.time()
predictions = model.predict(test_data)
predict_end = time.time()

# print(predictions)
for prediction in predictions:
	if prediction[0]>prediction[1]:
		result.append(1)
	else:
		result.append(0)
explicit_durations = []
for data in zip(list1,timestamps,result):
	if data[2] == 1:
		explicit_durations.append(data[1])
		# print(data[0],data[1])
if len(explicit_durations) > 0:
	conditions = []
	last_explicit_duration = 0
	for duration in explicit_durations:
		if float(duration)-last_explicit_duration<1:
			conditions.append("between(t,{},{})".format(float(last_explicit_duration),float(duration)+0.1))
		else:
			conditions.append("between(t,{},{})".format(float(duration),float(duration)+0.1))
		last_explicit_duration = float(duration)
	final_condition = "+".join(conditions)
	# print(final_condition)
	os.system("ffmpeg -i {} -q:v 1 -qmin 1 -filter_complex \"boxblur=90.0:enable='if({},1,0)\" -codec:a copy test.avi | vlc test.avi".format(video,final_condition))
# time2 = time.time()
# total = time2-time1
#
# print(total)
ext_time = ext_end - ext_start
prediction_time = predict_end - predict_start

print(ext_time)
print(prediction_time)
