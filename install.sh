#!/bin/bash
python --version
pip install decord
pip install opencv-python==4.8.0.74
pip install -U openmim
mim install mmcv-full==1.5.0
mim install mmdet==2.23.0
mim install mmpose==0.24.0