import numpy as np
import scipy.io
import ipdb

af = scipy.io.loadmat("c1p8.mat")
stim = af["stim"]
rho = af["rho"]

win = 40
spikes = np.where(rho == 1)[0]
spikes = spikes[spikes >= 40]
inputs = np.zeros((spikes.shape[0], win))

# iterate through the spiking data
for s_i in xrange(spikes.shape[0]):
    s_t = spikes[s_i]
    inputs[s_i] = stim[s_t-win:s_t].reshape((40,))

# average it and plot it    
in_avg = np.average(inputs, axis=0)
ipdb.set_trace()
plt.plot(in_avg)
plt.show()