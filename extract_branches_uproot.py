#! /usr/bin/env python3
import uproot
from tqdm import tqdm
import argparse
import awkward
import concurrent.futures
import os
import numpy as np
import pickle
import json


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', nargs='+', required=True)
    parser.add_argument('-v', '--variables', nargs='+', required=True)
    parser.add_argument('-k', '--key', type=str)
    parser.add_argument('-o', '--output', type=str)
    parser.add_argument('-j', '--jobs', type=int, default=1)
    parser.add_argument('-b', '--bins', type=int, default=150)
    # parser.add_argument('--chunksize', default=1_000_000, type=int)  not implemented yet
    args = parser.parse_args()

    executor = concurrent.futures.ThreadPoolExecutor(args.jobs)

    histos = {}

    variables = {}
    for v in args.variables:
        try:
            vardict = json.loads(v)
            variables.update(vardict)
        except:
            variables[v] = {}

    for f in tqdm(args.files):
        rf = uproot.open(f)
        tree = rf[args.key]
        data = {v.decode('utf-8'): d for v, d in tree.arrays(variables.keys(), executor=executor).items()}
        for v in variables.keys():
            if type(data[v]) == awkward.array.jagged.JaggedArray:
                data[v] = data[v][:, 0]
            data[v] = data[v][np.isfinite(data[v])]
            if not v in histos:
                histogram, bin_edges = np.histogram(
                    data[v], bins=args.bins, range=variables[v].get('range'))
                histos[v] = {
                    'histogram': histogram,
                    'bin_edges': bin_edges,
                }
            else:
                histogram, _ = np.histogram(data[v], bins=histos[v]['bin_edges'])
                histos[v]['histogram'] += histogram

    with open(args.output, 'wb') as f:
        pickle.dump(histos, f)
