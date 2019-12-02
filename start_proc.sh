#!/usr/bin/env bash

for folder in /home/erc/PycharmProjects/VideoCollection/csv/*
do
  for f in "$folder"/*
  do
    python3 data_proc.py "$f"
  done
done