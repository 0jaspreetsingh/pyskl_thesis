#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh
conda activate pys
python tools/data/custom_2d_skeleton.py --video-list /netscratch/jsingh/thesis/datasets/AUTHUAVGestureDatasetVideos_fps-15/uav_dfki_dataset.list --out /netscratch/jsingh/thesis/datasets/AUTHUAVGestureDatasetVideos_fps-15/uavgesture_annos.pkl --non-dist