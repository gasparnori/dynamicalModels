import numpy as np


class Input(object):
    def __init__(self, parameters, type):
        if (type=="sine"):
            self.init_sin(parameters)
        else:
            self.init_lin(parameters)

    def init_sin(self, parameters):
        self.freq=60
        self.I0=0.0
        self.Ain=2.0

        self.stim_curr = np.zeros(int(parameters.samples))
        self.times = np.linspace(parameters.stim_start, parameters.stim_start + parameters.stim_length, parameters.samples)
        self.stim_curr[parameters.stim_start: parameters.stim_start + parameters.stim_length] = self.I0
        self.stim_current=self.stim_curr+[self.Ain*np.sin(2*np.pi*self.freq * (i/parameters.samples)) for i in self.times]
        #self.data2=[i*2 for i in self.data]

    def init_lin(self, parameters):
        self.times = np.linspace(parameters.stim_start, parameters.stim_start + parameters.stim_length,
                                 parameters.samples)
        self.data = [i for i in self.times]
       # self.data2 = [i * 2 for i in self.data]