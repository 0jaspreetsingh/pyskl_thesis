#!/bin/bash
srun \
  --container-image=/netscratch/jsingh/pyskl.sqsh \
  bash -c 'fc -l -n' | sed 's/^\s*//' > scripts/installpyskl.sh