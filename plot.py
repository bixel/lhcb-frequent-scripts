import pickle
import os
import matplotlib.pyplot as plt
import numpy as np

WORKDIR = '/ceph/groups/e5a/users/kheinicke/b2oc/dsk-run2/'
TITLES = {
    'lab0_LifetimeFit_ctau': {
        'xlabel': '',
    },
}

with open(os.path.join(WORKDIR, 'OFFLINE-20152016-comparison.pkl'), 'rb') as f:
    histos20152016 = pickle.load(f)

with open(os.path.join(WORKDIR, 'OFFLINE-2017-comparison.pkl'), 'rb') as f:
    histos2017 = pickle.load(f)

with open(os.path.join(WORKDIR, 'OFFLINE-2018-comparison.pkl'), 'rb') as f:
    histos2018 = pickle.load(f)

for label, d in histos20152016.items():
    bins = d['bin_edges']
    content = d['histogram']
    width = bins[1] - bins[0]
    plt.step(bins[:-1], content / content.sum(), where='mid', label='2015 + 2016')
    content2017 = histos2017[label]['histogram']
    plt.errorbar(
        bins[:-1] + width / 4,
        content2017 / content2017.sum(),
        xerr=width / 4,
        yerr=np.sqrt(content2017) / content2017.sum(),
        fmt='C1,',
        label='2017',
    )
    content2018 = histos2018[label]['histogram']
    plt.errorbar(
        bins[:-1] + 2 * width / 4,
        content2018 / content2018.sum(),
        xerr=width / 4,
        yerr=np.sqrt(content2018) / content2018.sum(),
        fmt='C2,',
        label='2018',
    )
    plt.yscale('log')
    plt.xlim(bins[0], bins[-1])
    plt.legend(loc='best')
    plt.savefig(os.path.join(WORKDIR, 'hist-{}.pdf'.format(label)))
    plt.clf()
