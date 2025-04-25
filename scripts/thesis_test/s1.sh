#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh
conda activate pys
# Directory to append to PYTHONPATH
NEW_PATH="/home/jsingh/projects/thesis/code/pyskl_thesis/pyskl"

# Append the new path to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$NEW_PATH

# Optional: Print the PYTHONPATH to verify
echo "Updated PYTHONPATH: $PYTHONPATH"
python /home/jsingh/projects/thesis/code/pyskl_thesis/tools/test.py configs/posec3d/thesis/limb_s1.py --out /netscratch/jsingh/thesis_dataset/full_dataset/skletons/splits/pyskl/work_dirs/posec3d/slowonly_r50_ntu60_xsub/limb_s1/testpredictions.json