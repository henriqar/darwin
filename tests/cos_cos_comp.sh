#!/bin/bash
# file name: htcondor.sh

gcc cos_cos.c -lm -o cos_cos
./cos_cos $@

