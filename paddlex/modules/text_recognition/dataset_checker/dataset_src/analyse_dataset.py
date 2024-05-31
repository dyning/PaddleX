# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2024 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
Author: PaddlePaddle Authors
"""

import os
import json
import math
import platform
from pathlib import Path

from collections import defaultdict
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib import font_manager

from .....utils.file_interface import custom_open
from ....utils.fonts import PINGFANG_FONT_FILE_PATH


def simple_analyse(dataset_path, images_dict):
    """
    Analyse the dataset samples by return image path and label path

    Args:
        dataset_path (str): dataset path
        ds_meta (dict): dataset meta
        images_dict (dict): train, val and test image path

    Returns:
        tuple: tuple of sample number, image path and label path for train, val and text subdataset.
    
    """
    tags = ['train', 'val', 'test']
    sample_cnts = defaultdict(int)
    img_paths = defaultdict(list)
    res = [None] * 6

    for tag in tags:
        file_list = os.path.join(dataset_path, f'{tag}.txt')
        if not os.path.exists(file_list):
            if tag in ('train', 'val'):
                res.insert(0, "数据集不符合规范，请先通过数据校准")
                return res
            else:
                continue
        else:
            with custom_open(file_list, 'r') as f:
                all_lines = f.readlines()

            # Each line corresponds to a sample
            sample_cnts[tag] = len(all_lines)
            img_paths[tag] = images_dict[tag]

    return ("完成数据分析", sample_cnts[tags[0]], sample_cnts[tags[1]],
            sample_cnts[tags[2]], img_paths[tags[0]], img_paths[tags[1]],
            img_paths[tags[2]])


def deep_analyse(dataset_path, output_dir):
    """class analysis for dataset"""
    tags = ['train', 'val', 'test']
    all_instances = 0
    labels_cnt = {}
    x_max = []
    classes_max = []
    for tag in tags:
        image_path = os.path.join(dataset_path, f'{tag}.txt')
        if tag == 'test' and not os.path.exists(image_path):
            cnts_test = None
            continue
        str_nums = []
        with custom_open(image_path, 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip().split("\t")
            if len(line) != 2:
                print(f"Error in {line}.")
                continue
            str_nums.append(len(line[1]))
        max_length = min(100, max(str_nums))
        start = 0
        for i in range(1, math.ceil((max_length / 5))):
            stop = i * 5
            num_str = sum(start < i <= stop for i in str_nums)
            labels_cnt[f'{start}-{stop}'] = num_str
            start = stop
        if sum(max_length < i for i in str_nums) != 0:
            labels_cnt[f'> {max_length}'] = sum(max_length < i
                                                for i in str_nums)
        if tag == 'train':
            cnts_train = [cat_ids for cat_name, cat_ids in labels_cnt.items()]
            x_train = np.arange(len(cnts_train))
            if len(x_train) > len(x_max):
                x_max = x_train
                classes_max = [
                    cat_name for cat_name, cat_ids in labels_cnt.items()
                ]
        elif tag == 'val':
            cnts_val = [cat_ids for cat_name, cat_ids in labels_cnt.items()]
            x_val = np.arange(len(cnts_val))
            if len(x_val) > len(x_max):
                x_max = x_val
                classes_max = [
                    cat_name for cat_name, cat_ids in labels_cnt.items()
                ]
        else:
            cnts_test = [cat_ids for cat_name, cat_ids in labels_cnt.items()]
            x_test = np.arange(len(cnts_test))
            if len(x_test) > len(x_max):
                x_max = x_test
                classes_max = [
                    cat_name for cat_name, cat_ids in labels_cnt.items()
                ]

    width = 0.3 if not cnts_test else 0.2

    # bar
    os_system = platform.system().lower()
    if os_system == "windows":
        plt.rcParams['font.sans-serif'] = 'FangSong'
    else:
        font = font_manager.FontProperties(
            fname=PINGFANG_FONT_FILE_PATH, size=15)
    fig, ax = plt.subplots(figsize=(10, 5), dpi=120)
    ax.bar(x_train,
           cnts_train,
           width=0.3 if not cnts_test else 0.2,
           label='train')
    ax.bar(x_val + width,
           cnts_val,
           width=0.3 if not cnts_test else 0.2,
           label='val')
    if cnts_test:
        ax.bar(x_test + 2 * width, cnts_test, width=0.2, label='test')
    plt.xticks(
        x_max + width / 2 if not cnts_test else x_max + width,
        classes_max,
        rotation=90)
    ax.set_xlabel(
        '文本字长度区间',
        fontproperties=None if os_system == "windows" else font,
        fontsize=12)
    ax.set_ylabel(
        '图片数量',
        fontproperties=None if os_system == "windows" else font,
        fontsize=12)

    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    width, height = fig.get_size_inches() * fig.get_dpi()
    pie_array = np.frombuffer(
        canvas.tostring_rgb(), dtype='uint8').reshape(
            int(height), int(width), 3)
    fig1_path = os.path.join(output_dir, "histogram.png")
    cv2.imwrite(fig1_path, pie_array)

    return {"histogram": "histogram.png"}
