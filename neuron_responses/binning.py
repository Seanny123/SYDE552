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

bins = np.arange(0, 3.0, 1.0)
multi_trial_rate = np.zeros((bins.shape[0] - 1))
for z_i in range(better_zd.shape[0]):
    #ipdb.set_trace()
    hist_res = np.histogram(better_zd[0], bins=bins)[0]
    assert np.sum(hist_res) == better_zd[0].shape[0]
    multi_trial_rate += hist_res