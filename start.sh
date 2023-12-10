#!/bin/bash

python -m venv myEnv

souce myEnv/Scripts/activate #windows

#install python dependencies
cd python/
pip install -r requirements.txt