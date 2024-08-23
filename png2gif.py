#!/usr/bin/env python3

import imageio
import os
import argparse


def create_gif(image_list, gif_name, fps):
    frames=[]
    for image_name in image_list:
        print('read', image_name)
        frames.append(imageio.v2.imread(image_name, pilmode='RGBA'))
    imageio.mimsave(gif_name, frames, fps=fps, loop=0)


def seek_imagename(suffix):
    image_list = []
    allfile_name = os.listdir()
    for i in allfile_name:
        if os.path.splitext(i)[1] == suffix:
            image_list.append(i)
    image_list.sort()
    return image_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog = 'python3 png2gif.py',
        description = 'Build a GIF from PNGs.')
    parser.add_argument('--fps', default=10, type=int,
        help='number of frames per second')
    image_list = seek_imagename('.png')
    gif_name = 'animation.gif'
    args = parser.parse_args()
    create_gif(image_list, gif_name, args.fps)
