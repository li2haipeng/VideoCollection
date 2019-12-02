#!/usr/bin/env bash

for f in pcapFiles/2/*.pcap
do
  python3 autocollection_pcap2csv.py "$f" 10.63.7.178 csv
done