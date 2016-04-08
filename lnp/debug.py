import numpy as np
import scipy
from scipy.signal import lti
import ipdb

def synthetic_neuron(drive):
    """
    Simulates a mock neuron with a time step of 1ms.
    Arguments:
    drive - input to the neuron (expect zero mean; SD=1)
    Returns:
    rho - response function (0=non-spike and 1=spike at each time step)
    """
    dt = .001
    T = dt*len(drive)
    time = np.arange(0, T, dt)
    lagSteps = int(.02/dt)
    drive = np.concatenate((np.zeros(lagSteps), drive[lagSteps:]))
    system = scipy.signal.lti([1], [.03**2, 2*.03, 1])
    _, L, _ = scipy.signal.lsim(system, drive[:,np.newaxis], time)
    rate = np.divide(30, 1 + np.exp(50*(.05-L)))
    spikeProb = rate*dt
    return np.random.rand(len(spikeProb)) < spikeProb

def stavg(stim, resp, win=40):
    spikes = np.where(resp == 1)[0]
    spikes = spikes[spikes >= 40]
    inputs = np.zeros((spikes.shape[0], win))

    for s_i in xrange(spikes.shape[0]):
        s_t = spikes[s_i]
        ipdb.set_trace()
        inputs[s_i] = stim[s_t-win:s_t].reshape((win,))

    return np.average(inputs, axis=0)

white_vals = np.random.normal(0, 1, size=100)
white_noise = np.zeros(100*1000)

# how do I this without a for-loop?
for w_i in xrange(white_vals.shape[0]):
    white_noise[w_i*1000:(w_i+1)*1000] = white_vals[w_i]

n_res = synthetic_neuron(white_noise)
in_avg = stavg(white_noise, n_res, win=200)