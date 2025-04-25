#!/bin/bash

#SBATCH --nodes=1               # Number of nodes or servers. See: http://koeln.kl.dfki.de:3000/d/slurm-resources/resources?orgId=1&refresh=15s
#SBATCH --ntasks-per-node=1     # Number of task in each node, we want 1 
#SBATCH --cpus-per-task=4       # We want 4 cores for this job.
#SBATCH --mem-per-cpu=36gb      # each core to have 16 Gb RAM
#SBATCH --gres=gpu:1            # We want 4 GPUs in each node for this job.
#SBATCH --partition=A100-40GB,A100-80GB,A100-IML,A100-IN,A100-PBR,A100-PCI,A100-RP,A100-SDS,H100,H100-PCI,H100-SEE,H100-SLT,H100-SLT-NP,H100-Trails,H200,H200-DA,H200-SDS,L40S,L40S-DSA
#SBATCH --job-name=p3
#SBATCH -e ./out/R-%x.%j.out
#SBATCH -o ./out/R-%x.%j.out
#SBATCH --open-mode=append

NOW=$( date '+%F-%H-%M-%S' )
JOB_NAME=p3

srun -K\
  --container-mounts="`pwd`":"`pwd`",/netscratch/$USER:/netscratch/$USER,/ds:/ds:ro,/home/jsingh/projects/thesis/datasets,/home/jsingh/projects/thesis/code/pyskl_thesis \
  --container-image=/netscratch/jsingh/pyskl7.sqsh \
  --container-workdir="`pwd`" \
  /home/jsingh/projects/thesis/code/pyskl_thesis/scripts/thesis/p3.sh