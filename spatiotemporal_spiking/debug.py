import numpy as np
import matplotlib.pyplot as plt
import ipdb

class SpikingLif(object):
    def __init__(self, dt=0.001):
        self.refac_time = 0.0
        self.t_ref = 0.002
        self.refac = True
        self.dt = dt
        
        self.resist = 1e6
        self.cap = 10e-9
        self.k_pot = -0.075
        self.leak_pot = -0.065
        self.membrane_area = 0.1
        
        
        self.potential = 0.0
        self.reset_pot = -0.070
        self.spk_pot = -0.055
        
        self.adapt_cond = 0.0
        self.t_adapt = 0.1
        self.adapt_inc = 1e-9

        # for debugging
        self.spk_count = 0

    def spike(self, current):
        if(self.refac == False):
            dV = (
                    1/(self.resist*self.cap) * (self.leak_pot + current/self.resist*self.membrane_area - self.potential) +
                    (self.adapt_cond/self.cap) * (self.k_pot - self.potential)
            )*self.dt
            self.potential += dV
            print(dV)
            if self.spk_count > 0:
                ipdb.set_trace()
            
            dg = -(self.adapt_cond / self.t_adapt) * self.dt
            self.adapt_cond += dg
            
            # If we've reached the threshold, spike
            if(self.potential >= self.spk_pot):
                #ipdb.set_trace()
                # start the refactory period and reset the potential
                self.refac = True
                self.potential = self.reset_pot
                return [2.0, self.adapt_cond]
            return [self.potential, self.adapt_cond]
        else:
            # increment the refactory period
            self.refac_time += self.dt
            if(self.refac_time >= self.t_ref):
                # if we've reached the maximum refactory period, reset it
                self.refac = False
                self.refac_time = 0.0

                # also increase the spike adaptation
                self.adapt_cond += self.adapt_inc

                self.spk_count += 1

            return [self.reset_pot, self.adapt_cond]

input_current = 1.1e-9

step = 5e-4
t_range = np.arange(0, 0.5, step)
spk_lif = SpikingLif(dt=step)
spk_res = []

for t in list(t_range):
    spk_res.append(np.array(spk_lif.spike(input_current)))
spk_res = np.array(spk_res)