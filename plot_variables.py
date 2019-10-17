import root_pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import argparse

import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True  # noqa


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', nargs='+', required=True)
    parser.add_argument('-v', '--variables', nargs='+', required=True)
    parser.add_argument('-k', '--key', type=str)
    parser.add_argument('-o', '--output', type=str)
    parser.add_argument('--chunksize', default=100_000, type=int)
    args = parser.parse_args()

    flatten_columns, numeric_columns = [], []
    df_head = root_pandas.read_root(args.files, columns=args.variables,
                                    key=args.key, stop=1)
    for c in df_head.columns:
        if type(df_head[c].iloc[0]) == np.ndarray:
            flatten_columns.append(c)
        else:
            numeric_columns.append(c)

    zip_generator = zip(*([
            root_pandas.read_root(
                args.files,
                key=args.key,
                columns=numeric_columns,
                chunksize=args.chunksize
            )
        ]
        + [
            root_pandas.read_root(args.files, key=args.key, columns=[c], flatten=[c],
                                  chunksize=args.chunksize)
            for c in flatten_columns
        ])
    )
    entries = 0
    for f in args.files:
        tf = ROOT.TFile(f)
        tt = tf.Get(args.key)
        entries += tt.GetEntries()
    full_df = pd.DataFrame()
    for dfs in tqdm(zip_generator, total=entries // args.chunksize):
        for df in dfs[1:]:
            df.query('__array_index==0', inplace=True)
            df.drop(columns=['__array_index'], inplace=True)
            df.reset_index(inplace=True, drop=True)
        all_cols = pd.concat(dfs, axis=1)
        full_df = pd.concat([full_df, all_cols])
    full_df.to_root(args.output)
