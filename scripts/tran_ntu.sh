#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh
conda activate pys
python tools/train.py configs/posec3d/slowonly_r50_ntu60_xsub/limb.py --validate --test-last --test-best