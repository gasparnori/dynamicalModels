import numpy as np
import cellParams
import general_params

class Cell(object):
    def __init__(self, index, stim_current):
        self.index=index
        print "solving Hodcp.gKin-Huxley model"
        cp=cellParams.CellParams()
        p=general_params.Params()
        #Voltage dependent functions
        #Na activation gating variable (probability)
        #m(V)=1/(1+np.exp(-(V+40)/9))
        #taum=0.3
        # Na inactivation gating variable
        # h(V) = 1 / (1 + np.exp((V + 62) / 10))
        # tauh=1+11/(1+np.exp((V+62)/10))
        # K activation gating variable
        # n(V) = 1 / (1 + np.exp(-(V + 53) / 16))
        # taun=1+6/(1+np.exp((V + 53) / 16))


        #time dependent functions
        #dn/dt=(ninf-n)/taun
        #dm/dt=(minf-m)/taum
        #dh/dt=(hinf-n)/tauh



        #time dependedent functions
        self.V = np.zeros(int(p.samples))
        self.n = np.zeros(int(p.samples))
        self.m = np.zeros(int(p.samples))
        self.h = np.zeros(int(p.samples))

        # initial condition
        self.V[0] = cp.V0
        self.n[0]=cp.n0
        self.m[0]=cp.m0
        self.h[0]=cp.h0

        #Hodcp.gKin-Huxley
        #cm*dV/dt=-cp.gNa*np.exp(m,3)*h*(V-cp.ENa)-cp.gK*np.exp(n,4)*(V-cp.EK)-gL*(V-EL)
        for j in range(0, int(p.samples - 1)):
            #step 0:
            vj=self.V[j]

           # self.minf[j] = 1 / (1 + np.exp(-(vj + 40) / 9))
           # self.taum[j]=0.3
            mj=self.m[j]

            #self.hinf[j] = 1 / (1 + np.exp((vj + 62) / 10))
            #self.tauh[j]=1+11/(1+np.exp((vj+62)/10))
            hj=self.h[j]

           # self.ninf[j] = 1 / (1 + np.exp(-(vj + 53) / 16))
           # self.taun[j]=1+6/(1+np.exp((vj + 53) / 16))
            nj=self.n[j]



            #step 1: calculate K1
            K1n=(1 / (1 + np.exp(-(vj + 53) / 16))-self.n[j])/(1+6/(1+np.exp((vj + 53) / 16)))
            K1m=(1 / (1 + np.exp(-(vj + 40) / 9))-self.m[j])/0.3
            K1h=( 1 / (1 + np.exp((vj + 62) / 10))-self.h[j])/(1+11/(1+np.exp((vj+62)/10)))

            K1v = (-cp.gNa*np.power(mj,3)*hj *(vj-cp.ENa) -cp.gK*np.power(nj, 4)*(vj-cp.EK) -cp.gL*(vj-cp.EL)+stim_current[j])/cp.cm

            #step 2: calculate a
            an =nj+p.dt * K1n
            am =mj+p.dt * K1m
            ah =hj+p.dt * K1h
            av = vj + p.dt * K1v

            #step 3.1: update inf values (according to av)
            aminf=1 / (1 + np.exp(-(av + 40) / 9))
            ahinf=1 / (1 + np.exp((av + 62) / 10))
            aninf=1 / (1 + np.exp(-(av+ 53) / 16))

            tauminf=0.3
            tauhinf=1+11/(1+np.exp((av+62)/10))
            tauninf=1+6/(1+np.exp((av + 53) / 16))

            #step 3.2: update n, m, h values
            K2n = (aninf - an) / tauninf
            K2m = (aminf - am) / tauminf
            K2h = (ahinf - ah) / tauhinf

            # step 3.3: replace vj with av
            K2v=(-cp.gNa*np.power(am,3)*ah*(av-cp.ENa)-cp.gK*np.power(an,4)*(av-cp.EK)-cp.gL*(av-cp.EL)+stim_current[j+1])/cp.cm

            #step 4: calculate V
            self.V[j + 1] = vj + p.dt / 2 * (K1v + K2v)
            self.n[j + 1] = self.n[j] + p.dt / 2 * (K1n + K2n)
            self.m[j + 1] = self.m[j] + p.dt / 2 * (K1m + K2m)
            self.h[j + 1] = self.h[j] + p.dt / 2 * (K1h + K2h)