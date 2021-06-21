#!/bin/bash
path="$1"

cd $path

git config --global credential.helper store
git config --global credential.helper cache