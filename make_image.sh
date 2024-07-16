#!/bin/bash

#SBATCH --nodes=1               # Number of nodes or servers. See: http://koeln.kl.dfki.de:3000/d/slurm-resources/resources?orgId=1&refresh=15s
#SBATCH --ntasks-per-node=1     # Number of task in each node, we want 1 
#SBATCH --cpus-per-task=4       # We want 4 cores for this job.
#SBATCH --mem-per-cpu=24gb      # each core to have 16 Gb RAM
#SBATCH --gres=gpu:1            # We want 1 GPUs in each node for this job.
#SBATCH --partition=RTXA6000,V100-32GB,RTX3090  # Run this only in these mentioned GPUs. If you don't have any choice over GPUs, remove this parameter.
#SBATCH --job-name=custom_2d_skeleton
#SBATCH -e ./out/R-%x.%j.out
#SBATCH -o ./out/R-%x.%j.out
#SBATCH --open-mode=append

NOW=$( date '+%F-%H-%M-%S' )
JOB_NAME=custom_2d_skeleton

srun \
  --container-image=nvidia/cuda:11.3.0-cudnn8-runtime-centos8.sqsh \
  --container-save=/netscratch/$USER/pyskl.sqsh \
  --pty /bin/bash
  /home/jsingh/projects/thesis/code/pyskl_thesis/installconda.sh