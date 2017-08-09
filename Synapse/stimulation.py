import numpy as np


class stim(object):
    def __init__(self, numsamples, type):
        self.stim_start = 1000
        self.stim_length = 10000

        if (type=="sine"):
            self.init_sin(numsamples)
        else:
            self.init_lin(numsamples)

    def init_sin(self, numsamples):
        self.freq=60
        self.I0=0.0
        self.Ain=2.0

        self.stim_curr = np.zeros(int(numsamples))
        self.times = np.linspace(self.stim_start, self.stim_start + self.stim_length, numsamples)
        self.stim_curr[self.stim_start: self.stim_start + self.stim_length] = self.I0
        self.stim_current=self.stim_curr+[self.Ain*np.sin(2*np.pi*self.freq * (i/numsamples)) for i in self.times]
        #self.data2=[i*2 for i in self.data]

    def init_lin(self, numsamples):
        self.times = np.linspace(self.stim_start, self.stim_start + self.stim_length,
                                 numsamples)
        self.data = [i for i in self.times]
       # self.data2 = [i * 2 for i in self.data]