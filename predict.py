# USAGE
# python predict.py --input output/test_paths.txt

# import the necessary packages
from operator import mod
import tensorflow
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model
import numpy as np
import mimetypes
import argparse
import imutils
import pickle
import cv2
import os
import tensorflow as tf
import random
import string
from matplotlib import pyplot as plt
import boto3
# construct the argument parser and parse the arguments
import config

class predict:
	def get_random_string(length):
		letters = string.ascii_lowercase
		result_str = ''.join(random.choice(letters) for i in range(length))
		return result_str + '.jpg'

	def predict(self, path):
		uploads_dir = '/home/elidor/uploads/'
		results_dir = '/home/elidor/results/'
		bucket_name = "ml-experiments"
		folder_name = uploads_dir
		base_url = 'https://ml-experiments.fra1.digitaloceanspaces.com/images/'
		ap = argparse.ArgumentParser()
		ap.add_argument("-i", "--input",
						default='/home/elidor/uploads/upload.jpg',
						help="path to input image/text file of image paths")
		args = vars(ap.parse_args())

		# determine the input file type, but assume that we're working with
		# single input image
		filetype = mimetypes.guess_type(args["input"])[0]
		imagePaths = [args["input"]]
		tf.__version__

		# if the file type is a text file, then we need to process *multiple*
		# images
		if "text/plain" == filetype:
			# load the image paths in our testing file
			imagePaths = open(args["input"]).read().strip().split("\n")
			imagePath = path
		# load our object detector and label binarizer from disk
		print("[INFO] loading object detector...")
		with tf.device('/cpu:0'):
			model = load_model('/home/elidor/Documents/mobileNet.h5')
		# lb = pickle.loads(open(config.LB_PATH, "rb").read())

		# loop over the images that we'll be testing using our bounding box
		# regression model
		for imagePath in imagePaths:
			# load the input image (in Keras format) from disk and preprocess
			# it, scaling the pixel intensities to the range [0, 1]
			image = load_img(imagePath, target_size=(224, 224))
			image = img_to_array(image) / 255.0
			image = np.expand_dims(image, axis=0)

			# predict the bounding box of the object along with the class
			# label
			with tf.device('/cpu:0'):
				(boxPreds, labelPreds) = model.predict(image)
			(startX, startY, endX, endY) = boxPreds[0]

			# determine the class label with the largest predicted
			# probability
			i = np.argmax(labelPreds, axis=1)
			# Convert i to int so there's no type mismatch
			i = int(i)
			print(i)

			# label = lb.classes_[i][0]
			labels = ['Church of Saint Mary', 'The Monument of Apollonia', 'Theatre of Apollonia']
			print(i)
			label = labels[i]

			# load the input image (in OpenCV format), resize it such that it
			# fits on our screen, and grab its dimensions
			image = cv2.imread(imagePath)
			image = imutils.resize(image, width=600)
			(h, w) = image.shape[:2]

			# scale the predicted bounding box coordinates based on the image
			# dimensions
			startX = int(startX * w)
			startY = int(startY * h)
			endX = int(endX * w)
			endY = int(endY * h)

			# draw the predicted bounding box and class label on the image
			y = startY - 10 if startY - 10 > 10 else startY + 10
			cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX,
						0.65, (0, 255, 0), 2)
			cv2.rectangle(image, (startX, startY), (endX, endY),
						  (0, 255, 0), 2)
			# show the output image
			# Save the image that conmtains the bounding box
			pred = predict
			imgname = pred.get_random_string(12)
			# show the output image
			#cv2.imshow("Output", image)
			#Save the image that conmtains the bounding box
			write_name = '/home/elidor/results/'+imgname
			cv2.imwrite(write_name, image)
			#cv2.waitKey(0)

			session = boto3.session.Session()
			s3 = session.client('s3',
                        region_name='fra1',
                        endpoint_url='https://fra1.digitaloceanspaces.com',
                        aws_access_key_id='NS24MAUHRGZ56BDTJRSF',
                        aws_secret_access_key='Z6oz3oxKV47F91gEUoZNorpowqZ9gvLelsPKsfiTAXs')
			s3.upload_file(write_name, bucket_name, 'images/{}'.format(imgname), ExtraArgs={'ContentType': "image/jpg", 'ACL': "public-read"})

			return imgname, label

#p = predict()
#pred = p.predict()
#print(pred)
