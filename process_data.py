import pandas as pd
import os
import sys
import csv
from pathlib import Path
import numpy as np
import re


def toOneCsv(path):
    files = os.listdir(path)
    files.sort()
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
    for f in files:
        trace = []
        f_path = os.path.join(path, f)
        fp = Path(f_path)
        trace_name = fp.name[0:-4]
        nameRegex = re.compile(r'\d_')
        mo = nameRegex.search(trace_name)
        trace_name = trace_name[0: mo.start()+1]
        trace.append(trace_name)

        packets = pd.read_csv(f_path)
        size = packets.iloc[:,1]
        direction = packets.iloc[:,2]
        size = size.values
        direction = direction.values

        results = np.multiply(size,direction)
        pad = lambda a, i: a[0:i] if a.shape[0] >= i else np.hstack((a, np.zeros(i-a.shape[0])))
        results = pad(results, 15000)
        trace = trace.__add__(results.tolist())
        with open('video_lable.csv', 'a') as w:
            writer = csv.writer(w)
            writer.writerow(trace)
        print(f + 'is added')


def main(path):
    toOneCsv(path)


if __name__ == '__main__':
    main('csv')