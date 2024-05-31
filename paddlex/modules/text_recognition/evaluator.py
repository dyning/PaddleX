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
from pathlib import Path

from ..base.evaluator import BaseEvaluator
from .support_models import SUPPORT_MODELS


class TextRecEvaluator(BaseEvaluator):
    """ Text Recognition Model Evaluator """
    support_models = SUPPORT_MODELS

    def update_config(self):
        """update evalution config
        """
        if self.eval_config.log_interval:
            self.pdx_config.update_log_interval(self.eval_config.log_interval)

        self.pdx_config.update_dataset(self.global_config.dataset_dir,
                                       "MSTextRecDataset")
        label_dict_path = None
        if self.eval_config.get("label_dict_path"):
            label_dict_path = self.eval_config.label_dict_path
        else:
            label_dict_path = Path(
                self.eval_config.weight_path).parent / "label_dict.txt"
            if not label_dict_path.exists():
                label_dict_path = None
        if label_dict_path is not None:
            self.pdx_config.update_label_dict_path(label_dict_path)

    def get_eval_kwargs(self) -> dict:
        """get key-value arguments of model evalution function

        Returns:
            dict: the arguments of evaluation function.
        """
        return {
            "weight_path": self.eval_config.weight_path,
            "device": self.get_device()
        }
