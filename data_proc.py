import pandas as pd
import sys
import os
import csv
import re
import numpy as np
from pathlib import Path


def distribution(path):
    files = os.listdir(path)
    files.sort()
    dis={}
    for f in files:

        d = pd.read_csv(path + '/' + f)
        # print(d.shape)
        l = d.shape[0]
        if l in dis.keys():
            dis[l]+=1
        else:
            dis[l] = 1

    with open('video_round1_dis.csv', 'a') as w:
        writer = csv.DictWriter(w,dis.keys())
        writer.writeheader()
        writer.writerow(dis)

    # distribution = {3000:0,
    #                 4000:0,
    #                 5000:0,
    #                 6000:0,
    #                 7000:0,
    #                 8000:0,
    #                 9000:0,
    #                 10000:0,
    #                 11000:0,
    #                 12000:0,
    #                 13000:0,
    #                 14000:0,
    #                 15000:0,
    #                 10000000:0,}

def to_one_file(path):

    files = os.listdir(path)
    files.sort()
    for f in files:
        # data = pd.read_csv(Path + '/' + f)
        # data = data.values.tolist()
        # trace = [f[0:-4]]
        # for p in data:
        #     element = p[1]*p[2]
        #     trace.append(element)
        # with open('vdieo_round1.csv', 'a') as w:
        #     writer = csv.writer(w)
        #     writer.writerow(trace)
        trace = []
        f_path = os.path.join(path, f)
        fp = Path(f_path)
        trace_name = fp.name[0:-4]
        nameRegex = re.compile(r'\d_')
        mo = nameRegex.search(trace_name)
        trace_name = trace_name[0: mo.start() + 1]
        trace.append(trace_name)

        packets = pd.read_csv(f_path)
        size = packets.iloc[:, 1]
        direction = packets.iloc[:, 2]
        size = size.values
        direction = direction.values

        results = np.multiply(size, direction)
        pad = lambda a, i: a[0:i] if a.shape[0] >= i else np.hstack((a, np.zeros(i - a.shape[0])))
        results = pad(results, 12000)
        trace = trace.__add__(results.tolist())
        with open('video_lable.csv', 'a') as w:
            writer = csv.writer(w)
            writer.writerow(trace)
        # print(f + 'is added')
    print(path + ' finished!')


if __name__ == '__main__':
    P = sys.argv[1]
    to_one_file(P)
    # distribution(P)