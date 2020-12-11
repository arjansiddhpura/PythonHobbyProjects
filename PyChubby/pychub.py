import matplotlib.pyplot as plt

from pychubby.actions import Chubbify, Multiple, Pipeline, Smile, RaiseEyebrow, OpenEyes
from pychubby.detect import LandmarkFace

img_path = 'face.jpeg'
img = plt.imread(img_path)

lf = LandmarkFace.estimate(img)

a_per_face = Pipeline([Smile(0.33), OpenEyes(-0.05), RaiseEyebrow(scale=0.3, side='left'), Chubbify(-0.05)])

a_all = Multiple(a_per_face)

new_lf, _ = a_all.perform(lf)
new_lf.plot(show_landmarks=False, show_numbers=False)