"""
Makes a Random config.bmp for use in region generation in Sim City 4
"""
from PIL import Image
import numpy as np

import itertools


def create_bmp(height, width, file='config.bmp'):
    """Create bmp image from numpy array"""
    arr = np.zeros((height, width, 3), dtype=np.uint8)
    for h, w in itertools.product(range(height), range(width)):
        if np.any(arr[h, w, :] != 0):
            # check if a tile can be placed at all
            continue

        tile_type = np.random.randint(0,3)
        tile_size = 2 ** tile_type

        while (h + tile_size > height
               or w + tile_size > width
               or np.any(arr[h:h+tile_size, w:w+tile_size, :] != 0)): # overlaps previous
            tile_type -= 1
            tile_size = 2 ** tile_type
        for h_, w_ in itertools.product(range(h, h+tile_size), range(w, w+tile_size)):
            arr[h_, w_, tile_type] = 255

    img = Image.fromarray(arr, 'RGB')
    img.save(file)


if __name__ == '__main__':
    w, h = 4, 4

    create_bmp(h, w)
