import cv2
import numpy as np
import glob


def create_video(path, iterations, fps=15):
    size = ()
    img_array = []
    for i in range(1, iterations + 1):
        img = cv2.imread(path + f'/{i}.png')
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)
    # for filename in glob.glob(path + '/*.png'):
    #     img = cv2.imread(filename)
    #     height, width, layers = img.shape
    #     size = (width, height)
    #     img_array.append(img)

    out = cv2.VideoWriter(f'./Exports/{path}.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for image in img_array:
        out.write(image)

    out.release()


def create_dir(path):
    pass