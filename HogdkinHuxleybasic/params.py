import numpy as np

class Params(object):
    def __init__(self):
        self.samples=10000.0
        self.alpha=4
        self.eps=0.1#, 0.01]
        self.gamma=-10.0 #np.linspace (-10, 10, num=30)
        self.time_max=500.0
        self.v0=0.01
        self.w0=1.5

        #Hodgkin-Huxley
        self.n0=0.
        self.m0=0.0
        self.h0=0.0
        self.Volt0=-70.0
        self.dt = self.time_max / self.samples
        print self.dt

        #stimulation not working
        self.stim_start=1000
        self.I0=6.0
        self.stim_length=10000

        #self.stim_curr[self.stim_start: self.stim_length]=[self.I0 for i in range(0, self.stim_length)]

       # print self.stim_curr[self.stim_start-10 : self.stim_start+self.stim_length+10]
        #print self.dt
        #self.dt=np.linspace (1, 20, num=self.samples)