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
import os.path as osp
from pathlib import Path
from collections import defaultdict, Counter

from PIL import Image
import json
from pycocotools.coco import COCO

from ...base.dataset_checker import BaseDatasetChecker
from .dataset_src import check, convert, split_dataset, deep_analyse

from ..support_models import SUPPORT_MODELS


class COCODatasetChecker(BaseDatasetChecker):
    """Dataset Checker for Object Detection Model
    """
    support_models = SUPPORT_MODELS
    sample_num = 10

    def get_dataset_root(self, dataset_dir: str) -> str:
        """find the dataset root dir

        Args:
            dataset_dir (str): the directory that contain dataset.

        Returns:
            str: the root directory of dataset.
        """
        anno_dirs = list(Path(dataset_dir).glob("**/images"))
        assert len(anno_dirs) == 1
        dataset_dir = anno_dirs[0].parent.as_posix()
        return dataset_dir

    def convert_dataset(self, src_dataset_dir: str) -> str:
        """convert the dataset from other type to specified type

        Args:
            src_dataset_dir (str): the root directory of dataset.

        Returns:
            str: the root directory of converted dataset.
        """
        converted_dataset_path = os.path.join(
            os.getenv("TEMP_DIR"), "converted_dataset")
        return convert(self.check_dataset_config.convert.src_dataset_type,
                       dataset_dir, converted_dataset_path)

    def split_dataset(self, src_dataset_dir: str) -> str:
        """repartition the train and validation dataset

        Args:
            src_dataset_dir (str): the root directory of dataset.

        Returns:
            str: the root directory of splited dataset.
        """
        return split_dataset(
            dataset_dir, self.check_dataset_config.split.split_train_percent,
            self.check_dataset_config.split.split_val_percent)

    def check_dataset(self, dataset_dir: str,
                      sample_num: int=sample_num) -> dict:
        """check if the dataset meets the specifications and get dataset summary

        Args:
            dataset_dir (str): the root directory of dataset.
            sample_num (int): the number to be sampled.
        Returns:
            dict: dataset summary.
        """
        return check(dataset_dir, self.global_config.output)

    def analyse(self, dataset_dir: str) -> dict:
        """deep analyse dataset

        Args:
            dataset_dir (str): the root directory of dataset.

        Returns:
            dict: the deep analysis results.
        """
        return deep_analyse(dataset_dir, self.global_config.output)

    def get_show_type(self) -> str:
        """get the show type of dataset

        Returns:
            str: show type
        """
        return "image"

    def get_dataset_type(self) -> str:
        """return the dataset type

        Returns:
            str: dataset type
        """
        return "COCODetDataset"
