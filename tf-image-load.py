from __future__ import absolute_import, division, print_function

import IPython.display as display
import random
import matplotlib.pylab as plt

import tensorflow as tf
# import tensorflow_hub as hub


from tensorflow.keras import layers

import pathlib
""" data_root = tf.keras.utils.get_file('flower_photos','https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz', untar=True)
print(data_root) """

# local_file = 'E:\\Tutorials\\AI\\ML\\Tutorials\\Tensorflow\\venv\\apps\\flower_photos\\flower_photos'
local_file = 'E:/Tutorials/AI/ML/Tutorials/Tensorflow/venv/apps/flower_photos/flower_photos'

data_root = pathlib.Path(local_file)
print(data_root)

for item in data_root.iterdir():
    print(item)

all_image_paths = list(data_root.glob('*/*'))
all_image_paths = [str(path) for path in all_image_paths]
random.shuffle(all_image_paths)

image_count = len(all_image_paths)
print(image_count)
# print(all_image_paths[:10])

attributions = (
    data_root/"LICENSE.txt").read_text(encoding="utf8").splitlines()[4:]
attributions = [line.split(' CC-BY') for line in attributions]
attributions = dict(attributions)


def caption_image(image_path):
    image_rel = pathlib.Path(image_path).relative_to(data_root)
    print(image_rel)

    str_img = str(image_rel)
    print(str_img)
    # print(attributions)

    str_img = str_img.replace("//", "\\")
    str_img = str_img.replace("/", "\\")

    img_attr = attributions[str_img]
    print(img_attr)

    img = img_attr.split(' - ')
    print(img)
    return "Image (CC BY 2.0) " + ' - '.join(img[:-1])


for n in range(3):
    image_path = random.choice(all_image_paths)
    display.display(display.Image(image_path))
    print(caption_image(image_path))
    print()
