#!/bin/bash

pkill -f "sh base/autoCommit.sh"
pkill -f "sh base/timeAutoCommit.sh"
pkill -f "sh base/filetimeAutoCommit.sh"
pkill -f "sh base/fileAutoCommit.sh"
pkill -f "sh base/fileNPercent.sh"