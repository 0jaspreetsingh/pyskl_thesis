#!/bin/bash

#SBATCH --nodes=1               # Number of nodes or servers. See: http://koeln.kl.dfki.de:3000/d/slurm-resources/resources?orgId=1&refresh=15s
#SBATCH --ntasks-per-node=1     # Number of task in each node, we want 1 
#SBATCH --cpus-per-task=4       # We want 4 cores for this job.
#SBATCH --mem-per-cpu=24gb      # each core to have 16 Gb RAM
#SBATCH --gres=gpu:4            # We want 4 GPUs in each node for this job.
#SBATCH --job-name=train_stgcn_pyskl_uav
#SBATCH -e ./out/R-%x.%j.out
#SBATCH -o ./out/R-%x.%j.out
#SBATCH --open-mode=append

NOW=$( date '+%F-%H-%M-%S' )
JOB_NAME=train_stgcn_pyskl_uav

srun -K\
  --container-mounts="`pwd`":"`pwd`",/netscratch/$USER:/netscratch/$USER,/ds:/ds:ro,/home/jsingh/projects/thesis/datasets,/home/jsingh/projects/thesis/code/pyskl_thesis \
  --container-image=/netscratch/jsingh/pyskl7.sqsh \
  --container-workdir="`pwd`" \
  /home/jsingh/projects/thesis/code/pyskl_thesis/scripts/train_stgcn_pyskl_uav.sh