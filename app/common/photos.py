import os
import re

from flask import current_app as app


def get_photos_list(filter_func):
    photos_dir = os.path.join(app.root_path, 'static/images/photos/full')
    filtered_images = filter(filter_func, os.listdir(photos_dir))
    photos_list = list(map(lambda x: {
        'filename': x,
        'group': re.match('[a-zA-z]*', x).group(0)
    }, filtered_images))
    return photos_list
