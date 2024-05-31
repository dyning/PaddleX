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
from random import shuffle

from .....utils.file_interface import custom_open


def split_dataset(root_dir, train_rate, val_rate, test_rate=0):
    """
    将图像数据集按照比例分成训练集、验证集和测试集，并生成对应的.txt文件。

    Args:
        root_dir (str): 数据集根目录路径。
        train_rate (int): 训练集占总数据集的比例（%）。
        val_rate (int): 验证集占总数据集的比例（%）。
        test_rate (int): 测试集占总数据集的比例（%）。

    Returns:
        str: 数据划分结果信息。
    """
    sum_rate = train_rate + val_rate + test_rate
    assert sum_rate == 100, \
    f"The sum of train_rate({train_rate}), val_rate({val_rate}) and test_rate({test_rate}) should equal 100!"
    assert train_rate > 0 and val_rate > 0, \
    f"The train_rate({train_rate}) and val_rate({val_rate}) should be greater than 0!"
    tags = ["train", "val", "test"]
    valid_path = False
    image_files = []
    for tag in tags:
        split_image_list = os.path.abspath(os.path.join(root_dir, f'{tag}.txt'))
        rename_image_list = os.path.abspath(
            os.path.join(root_dir, f'{tag}.txt.bak'))
        if os.path.exists(split_image_list):
            with custom_open(split_image_list, 'r') as f:
                lines = f.readlines()
            image_files = image_files + lines
            valid_path = True
            if not os.path.exists(rename_image_list):
                os.rename(split_image_list, rename_image_list)
            if test_rate == 0 and tag == "test" and os.path.exists(
                    split_image_list):
                os.remove(split_image_list)

    assert valid_path, \
    f"The files to be divided{tags[0]}.txt, {tags[1]}.txt or {tags[2]}.txt, do not exist in the dataset directory."

    shuffle(image_files)
    start = 0
    image_num = len(image_files)
    rate_list = [train_rate, val_rate, test_rate]
    for i, tag in enumerate(tags):

        rate = rate_list[i]
        if rate == 0:
            continue

        end = start + round(image_num * rate / 100)
        if sum(rate_list[i + 1:]) == 0:
            end = image_num

        txt_file = os.path.abspath(os.path.join(root_dir, tag + '.txt'))
        with custom_open(txt_file, 'w') as f:
            m = 0
            for id in range(start, end):
                m += 1
                f.write(image_files[id])
        start = end

    return root_dir
