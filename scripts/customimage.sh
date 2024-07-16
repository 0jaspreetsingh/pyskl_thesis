#!/bin/bash
srun \
  --mem=24gb \
  --container-image=/enroot/nvcr.io_nvidia_pytorch_20.12-py3.sqsh \
  --container-save=/netscratch/$USER/pyskl.sqsh \
  --pty /bin/bash