#!/bin/bash
conda env create -f pyskl.yaml
conda activate pyskl
pip install -e .