#!/usr/bin/env bash
## ip/timeout/iteration

for f in /home/erc/PycharmProjects/VideoCollection/list/round2/*.csv
  do
    for i in {70..199}
    do
      python3 loadDriver.py "$f" 10.63.7.178 180 "$i"
    done
  done

#for f in /home/erc/PycharmProjects/VideoCollection/list/round2/*.csv
#  do
#    python3 loadDriver.py "$f" 10.63.7.178 180 200
#  done