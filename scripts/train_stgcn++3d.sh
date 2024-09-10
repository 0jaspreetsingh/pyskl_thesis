#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh
conda activate pys
# Directory to append to PYTHONPATH
NEW_PATH="/home/jsingh/projects/thesis/code/pyskl_thesis/pyskl"

# Append the new path to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$NEW_PATH

# Optional: Print the PYTHONPATH to verify
echo "Updated PYTHONPATH: $PYTHONPATH"
python /home/jsingh/projects/thesis/code/pyskl_thesis/tools/train.py configs/stgcn++/stgcn++_ntu60_xsub_3dkp/b_uav.py --validate --test-last --test-best