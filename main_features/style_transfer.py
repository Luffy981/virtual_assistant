#!/usr/bin/env python3


import functools
import os
import datetime
import time

from matplotlib import gridspec
import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import cv2

print("TF Version: ", tf.__version__)
print("TF Hub version: ", hub.__version__)
print("Eager mode enabled: ", tf.executing_eagerly())
print("GPU available: ", tf.config.list_physical_devices('GPU'))


# @title Define image loading and visualization functions  { display-mode: "form" }

def crop_center(image):
  """Returns a cropped square image."""
  shape = image.shape
  new_shape = min(shape[1], shape[2])
  offset_y = max(shape[1] - shape[2], 0) // 2
  offset_x = max(shape[2] - shape[1], 0) // 2
  image = tf.image.crop_to_bounding_box(
      image, offset_y, offset_x, new_shape, new_shape)
  return image

@functools.lru_cache(maxsize=None)
def load_image(image_url, image_size=(256, 256), preserve_aspect_ratio=True):
  """Loads and preprocesses images."""
  # Cache image file locally.
  # image_path = tf.keras.utils.get_file(os.path.basename(image_url)[-128:], image_url)
  image_path = image_url
  # Load and convert to float32 numpy array, add batch dimension, and normalize to range [0, 1].
  img = tf.io.decode_image(
      tf.io.read_file(image_path),
      channels=3, dtype=tf.float32)[tf.newaxis, ...]
  img = crop_center(img)
  img = tf.image.resize(img, image_size, preserve_aspect_ratio=True)
  return img

def show_n(images, titles=('',)):
  n = len(images)
  image_sizes = [image.shape[1] for image in images]
  w = (image_sizes[0] * 6) // 320
  plt.figure(figsize=(w * n, w))
  gs = gridspec.GridSpec(1, n, width_ratios=image_sizes)
  for i in range(n):
    plt.subplot(gs[i])
    plt.imshow(images[i][0], aspect='equal')
    plt.axis('off')
    plt.title(titles[i] if len(titles) > i else '')
  plt.show()

def Streamming():
    # Video streaming
    video_capture = cv2.VideoCapture(0)
    
    TIMER = int(3)
    prev = time.time()
    while TIMER >= 0:
        ret, frame = video_capture.read()
        if ret == False:
            break
        frame = cv2.flip(frame, 1)

        # cv2.putText(frame, str(end_time), (70,70), cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0), 2, cv2.LINE_AA)# adding timer text

        font = cv2.FONT_HERSHEY_SIMPLEX
        if TIMER != 0:
            cv2.putText(frame, str(TIMER), 
                        (200, 250), font,
                        7, (0, 255, 255),
                        4, cv2.LINE_AA) 
        else:
            # Save the frame
            cv2.imwrite('camera.jpg', frame)

        cv2.imshow('Frame', frame)
        k = cv2.waitKey(1)
        # current time
        cur = time.time()
        if cur-prev >= 1:
            prev = cur
            TIMER = TIMER - 1
        if k == 27 & 0xFF:
            break
    video_capture.release()
    cv2.destroyAllWindows()
    
# @title Load example images  { display-mode: "form" }

def Pick_Style(tipo='one'):
    styles = {'one': './images/style/van_gogh_trees.jpg',
              'two': './images/style/picasso_self_portrait.jpg',
              'three': './images/style/picasso_weeping_woman.jpg',
              'four': './images/style/van_gogh_starry_night.jpg',
              'five': './images/style/derain_mountains_at_colloiure.jpg',
              'six': './images/style/van_gogh_van_gogh_road_cypress.jpg',
              'seven': './images/style/van_gogh_red_cabbages_and_onions.jpg'}
    content_image_url = './camera.jpg'  # @param {type:"string"}
    style_image_url = styles[tipo]  # @param {type:"string"}
    output_image_size = 384  # @param {type:"integer"}

    # The content image size can be arbitrary.
    content_img_size = (output_image_size, output_image_size)
    # The style prediction model was trained with image size 256 and it's the 
    # recommended image size for the style image (though, other sizes work as 
    # well but will lead to different results).
    style_img_size = (256, 256)  # Recommended to keep it at 256.

    content_image = load_image(content_image_url, content_img_size)
    style_image = load_image(style_image_url, style_img_size)
    style_image = tf.nn.avg_pool(style_image, ksize=[3,3], strides=[1,1], padding='SAME')
    # show_n([content_image, style_image], ['Content image', 'Style image'])


    # Load TF Hub module.

    hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
    hub_module = hub.load(hub_handle)


    outputs = hub_module(content_image, style_image)
    stylized_image = outputs[0]


    # Stylize content image with given style image.
    # This is pretty fast within a few milliseconds on a GPU.

    outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
    stylized_image = outputs[0]


    # Visualize input images and the generated stylized image.


    show_n([stylized_image], titles=['Stylized image'])

def Show_Styles():
    """
    Styles
    """
    styles = ['./images/style/van_gogh_trees.jpg',
              './images/style/picasso_self_portrait.jpg',
              './images/style/picasso_weeping_woman.jpg',
              './images/style/van_gogh_starry_night.jpg',
              './images/style/derain_mountains_at_colloiure.jpg',
              './images/style/van_gogh_van_gogh_road_cypress.jpg',
              './images/style/van_gogh_red_cabbages_and_onions.jpg']
    style_img_size = (256, 256)  # Recommended to keep it at 256.

    style_img = []
    for style in styles:
        style_image = load_image(style, style_img_size)
        style_image = tf.nn.avg_pool(style_image, ksize=[3,3], strides=[1,1], padding='SAME')
        style_img.append(style_image)

    show_n(style_img, ['Style 1', 'Style 2', 'Style 3', 'Style 4', 'Style 5', 'Style 6', 'Style 7'])

if __name__ == "__main__":
    pass
