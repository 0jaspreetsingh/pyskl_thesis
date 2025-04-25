#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh
conda activate pys
python tools/data/custom_2d_skeleton.py --video-list /home/jsingh/projects/thesis/code/pyskl_thesis/gesture_recognition_dataset_test.list --out /netscratch/jsingh/thesis_dataset/full_dataset/skletons/gesture_recognition_dataset_test.pkl --non-dist