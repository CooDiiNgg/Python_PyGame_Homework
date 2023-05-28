import pygame
import numpy as np


def map_to_array():
    dict_for_map = {}

    image_path = "Images/Map.png"
    image = pygame.image.load(image_path)
    width, height = image.get_width(), image.get_height()

    surface = pygame.Surface((width, height))
    surface.blit(image, (0, 0))
    data = pygame.surfarray.array3d(surface)
    data = np.swapaxes(data, 0, 1)


    array = np.zeros((height, width), dtype=int)
    x = 0
    for row in range(height):
        for col in range(width):
            pixel = tuple(data[row, col])
            if pixel in dict_for_map:
                array[row, col] = dict_for_map[pixel]
            else:
                dict_for_map[pixel] = x
                array[row, col] = x
                x += 1

    # save the whole array in file txt
    np.savetxt("map.txt", array, fmt="%d")


map_to_array()