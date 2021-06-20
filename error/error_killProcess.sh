#!/bin/bash
result=$(ps ax | grep exe_c.sh)
result2=$(ps ax | grep compile_c.sh)
result3=$(ps ax | grep exe_java.sh)
result4=$(ps ax | grep compile_java.sh)

#echo $result

pkill -f "sh exe_c.sh"
pkill -f "sh compile_c.sh"
pkill -f "sh exe_java.sh"
pkill -f "sh compile_java.sh"