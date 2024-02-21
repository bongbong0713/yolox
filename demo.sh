#!/bin/bash

for i in $(seq 918 930); do
    video_file="0${i}-쓰러짐.avi"
    python tools/demo.py video -f exps/example/mot/yolox_x_mix_testset_roboflow_bytetrack.py -c YOLOX_outputs/yolox_x_mix_testset_roboflow_bytetrack/best_ckpt.pth --path ../ByteTrack_jm/data/401_인증용DB_KISA/ext_data/files/$video_file --conf 0.6 --nms 0.45 --tsize 640 --save_result --device gpu
done