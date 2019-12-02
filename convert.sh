#!/usr/bin/env bash

for folder in /home/erc/PycharmProjects/2019_spring_data/video_pcapFiles/Round2/*
do
  for f in "$folder"/*
  do
    for p in "$f"/*.pcap
    do
      python3 autocollection_pcap2csv.py "$p" 10.63.7.178 "$f"
#      echo "$p"
    done
  done
done