import numpy as np
import scipy.io
import ipdb

af = scipy.io.loadmat("dir_tune.mat")
direc = af["direction"]
spike_t = af["spikeTimes"]
zero_deg = spike_t[direc == 0]

dirs = np.unique(direc)
d_spikes = [[] for _ in range(dirs.shape[0])] 

for d_i, d_val in enumerate(list(dirs)):
    # get the spikes for each trial
    tmp_spikes = spike_t[direc == 0]
    
    # filter spikes to only take into account 50 to 250ms
    filt_spikes = []
    for t_s in range(tmp_spikes.shape[0]):
        ipdb.set_trace()