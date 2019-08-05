#!/bin/bash
# file name: htcondor.sh

TIMETOWAIT="10"
echo "sleeping for $TIMETOWAIT seconds"

DARWINROOT="."
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
  -root)
    DARWINROOT="$2"
    shift # past argument
    shift # past value
    ;;
  -map1)    # unknown option
    MAP1="$2"
    shift # past argument
    shift # past value
    ;;
  -map2)
    MAP2="$2"
    shift
    shift
    ;;
esac
done

function prog() {
  echo -e "-map1 ${MAP1} -map2 ${MAP2} " 
  echo -e "-root $DARWINROOT "
  pushd .
  cd $DARWINROOT
  echo -e "${MAP1}\n${MAP2}" > output.txt
  popd
  /bin/sleep $TIMETOWAIT
}

prog
