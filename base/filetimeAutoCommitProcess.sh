#!/bin/bash
path="$1"

cd $path

crtime="$2"

n="$3"

sh filetimeAutoCommit.sh $path $crtime $n &