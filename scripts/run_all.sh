#!/bin/bash

for ((i=0; i<23; i++)){
  qsub -q gpu job_$i.sh
}

