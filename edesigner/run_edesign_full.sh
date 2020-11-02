#!/bin/bash
conda activate edesign
[ ! -d ./resources ] && mkdir ./resources
[ ! -d ./comps ] && mkdir ./comps
[ ! -d ./data ] && mkdir ./data
[ ! -d ./logs ] && mkdir ./logs
[ ! -d ./results ] && mkdir ./results
python e_bbt_creator.py 
python e_designer.py 
python lib_designer.py
python lib_design_interpreter.py 
