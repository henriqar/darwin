#!/bin/bash
# file name: htcondor.sh

TIMETOWAIT="10"
echo "sleeping for $TIMETOWAIT seconds"

DARWINROOT="."
OUT=""

while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -root)
    DARWINROOT="$2"
    shift # past argument
    shift # past value
    ;;
    -*)    # unknown option
    OUT+="$key\n"
    OUT+="$2\n"
    shift # past argument
    shift # past value
    ;;
esac
done

function prog() {
  echo -e $OUT 
  echo -e $DARWINROOT 
  pushd .
  cd $DARWINROOT
  echo -e $OUT > output.txt
  popd
  /bin/sleep $TIMETOWAIT
}

prog
