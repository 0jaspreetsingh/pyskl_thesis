#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh
conda activate pys
python tools/data/custom_2d_skeleton.py --video-list /netscratch/jsingh/thesis_dataset/full_dataset/label_studio/gesture_recognition_full_videos.list --out /netscratch/jsingh/thesis_dataset/full_dataset/skletons/gesture_recognition_dataset_full_videos_final.pkl --non-dist