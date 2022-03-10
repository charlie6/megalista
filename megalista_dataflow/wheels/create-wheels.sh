#!bin/bash

pip wheel ./setup.py -w ./wheels/packages
#pip wheel --no-deps -r ./megalista_dataflow/requirements-no-deps.txt -w ./wheels/packages