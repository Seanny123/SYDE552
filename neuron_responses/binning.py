import numpy as np
import scipy.io
import ipdb

af = scipy.io.loadmat("dir_tune.mat")
direc = af["direction"]
spike_t = af["spikeTimes"]
zero_deg = spike_t[direc == 0]

better_zd = []
for z_i in range(zero_deg.shape[0]):
    better_zd.append(zero_deg[z_i][0])
better_zd = np.array(better_zd)

bins = np.arange(0, 2.005, 0.005)
multi_trial_rate = np.zeros((bins.shape[0] - 1, better_zd.shape[0]))
for z_i in range(better_zd.shape[0]):
    for b_i in range(bins.shape[0]):
        filt = better_np.where(better_zd
        multi_trial_rate[b_i, z_i] = 