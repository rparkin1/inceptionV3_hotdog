#!/usr/bin/python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os

from IPython.display import Image, HTML, display

    
root = "images"
butions = dict(attributions)
   
def show_image(image_path):
    display(Image(image_path))
    
    image_rel = image_path.replace(root,'')
    caption = "Image " + ' - '.join(attributions[image_rel].split(' - ')[:-1])
    display(HTML("<div>%s</div>" % caption))
