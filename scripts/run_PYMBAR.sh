#!/bin/bash

#copy and rename dhdl.xvg files into new folder
mkdir dhdl_data_mbar
for ((i=0; i<23; i++)){
  cp Lambda_$i/Production_MD/md$i.xvg dhdl_data_mbar/dhdl.$i.xvg
}

#run pymbar
python /beegfs/work/workspace/ws/st_ac128541-logP-0/Programs/alchemical-analysis/alchemical_analysis/alchemical_analysis.py -d dhdl_data_mbar/ -q xvg -p dhdl -u kJ -v -w -g -t 323
