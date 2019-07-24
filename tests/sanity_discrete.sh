#!/bin/bash
# file name: htcondor.sh

TIMETOWAIT="10"
echo "sleeping for $TIMETOWAIT seconds"
echo $@ > output.txt
/bin/sleep $TIMETOWAIT

