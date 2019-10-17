#! /usr/bin/env python3
"""
Generate comparison plots. Either one plot per variable for all files
(default), or one plot per file with all variables (if you set
`--compare-files`.
"""
import uproot
import matplotlib.pyplot as plt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', nargs='+', required=True)
    parser.add_argument('-v', '--variables', nargs='+', required=True)
    parser.add_argument('-c', '--compare-files', action='store_true',
                        default=False)
    parser.add_argument('-o', '--output', type=str)
    args = parser.parse_args()

    if args.compare_files:
        for var in args.variables:
            for i, f in enumerate(args.files):
                rf = uproot.open(f)
                data = rf[rf.allkeys()[0]].array(var)
                plt.hist(data, bins='fd', label=str(i), density=True, alpha=0.5)
            plt.title(var)
            plt.legend(loc='best')
            plt.savefig(os.path.join(args.output, f'{var}.pdf'))
    else:
        pass
