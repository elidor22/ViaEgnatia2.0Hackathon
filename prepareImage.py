
import cv2
import matplotlib.pyplot as plt
from keras_preprocessing.image import load_img

imagePath = 'dataset/Monument of Agonothetes/2-10.jpg'
image = load_img(imagePath, target_size=(224, 224))

print('PIL image size', image.size)
plt.imshow(image)
plt.show()
