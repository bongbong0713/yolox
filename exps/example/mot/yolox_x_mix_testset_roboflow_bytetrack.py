# encoding: utf-8
import os
import random
import torch
import torch.nn as nn
import torch.distributed as dist

# from yolox.exp import BYTE_Exp as MyExp
from yolox.exp import Exp as MyExp
from yolox.data import get_yolox_datadir

class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.num_classes = 2
        self.depth = 1.33
        self.width = 1.25
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]
        self.data_dir = "/home/jhs/YOLOX/datasets"
        self.train_ann = "/home/jhs/YOLOX/datasets/annotations/merged_testset_roboflow_bytetrack.json"
        self.val_ann = "/home/jhs/YOLOX/datasets/annotations/val_half.json"    # change to train.json when running on training set
        self.input_size = (800, 1440)
        self.test_size = (800, 1440)
        self.random_size = (18, 32)
        self.max_epoch = 80
        self.print_interval = 20
        self.eval_interval = 5
        self.test_conf = 0.001
        self.nmsthre = 0.7
        self.no_aug_epochs = 10
        self.basic_lr_per_img = 0.0001 / 64.0
        self.warmup_epochs = 1
        self.save_history_ckpt = False