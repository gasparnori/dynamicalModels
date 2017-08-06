import numpy as np

class HoHu(object):
    def __init__(self, params):
        print "solving Hodgkin-Huxley model"
        gNa = 120.0  # mS/cm^2
        gK = 36.0  # mS/cm^2
        gL = 0.3  # 3333 Ohmcm^2
        EL = -50.6  # mV
        ENa = 55.0  # mV
        EK = -75.0  # mV
        cm=1.0   #uF/cm^2

        self.V = np.zeros(int(params.samples))
        self.n = np.zeros(int(params.samples))
        #self.ninf = np.zeros(1, int(params.samples))
        #self.taun = np.zeros(1, int(params.samples))

        self.m = np.zeros(int(params.samples))
        #self.minf = np.zeros(1, int(params.samples))
        #self.taum = np.zeros(1, int(params.samples))

        self.h = np.zeros(int(params.samples))
        #self.hinf = np.zeros(1, int(params.samples))
        #self.tauh = np.zeros(1, int(params.samples))

        # initial condition
        self.V[0] = params.Volt0
        self.n[0]=params.n0

        #self.ninf[0] = 1 / (1 + np.exp(-(self.V[0] + 53) / 16))
        #self.taun[0] = 1 + 6 / (1 + np.exp((self.V[0] + 53) / 16))
        self.m[0]=params.m0
        #self.minf[0] = 1 / (1 + np.exp(-(self.V[0] + 40) / 9))
        #self.taum[0] = 0.3

        self.h[0]=params.h0
        #self.hinf[0] = 1 / (1 + np.exp((self.V[0] + 62) / 10))
        #self.tauh[0] = 1 + 11 / (1 + np.exp((self.V[0] + 62) / 10))


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

        #Hodgkin-Huxley
        #cm*dV/dt=-gNa*np.exp(m,3)*h*(V-ENa)-gK*np.exp(n,4)*(V-Ek)-gL*(V-EL)
        for j in range(0, int(params.samples - 1)):
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

            K1v = (-gNa*np.power(mj,3)*hj *(vj-ENa) -gK*np.power(nj, 4)*(vj-EK) -gL*(vj-EL))/cm+params.stim_curr[j]

            #step 2: calculate a
            an =nj+params.dt * K1n
            am =mj+params.dt * K1m
            ah =hj+params.dt * K1h
            av = vj + params.dt * K1v

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
            K2v=(-gNa*np.power(am,3)*ah*(av-ENa)-gK*np.power(an,4)*(av-EK)-gL*(av-EL))/cm+params.stim_curr[j]

            #step 4: calculate V
            self.V[j + 1] = vj + params.dt / 2 * (K1v + K2v)
            self.n[j + 1] = self.n[j] + params.dt / 2 * (K1n + K2n)
            self.m[j + 1] = self.m[j] + params.dt / 2 * (K1m + K2m)
            self.h[j + 1] = self.h[j] + params.dt / 2 * (K1h + K2h)