import numpy as np

class Model1(object):
    def __init__(self, params):
        print "Model 1 solving..."
        #model: v'=-2*v^3+3*v^2
        self.output = np.zeros(int(params.samples))

        #initial condition
        self.output[0]= params.v0

        for j in range(0, int(params.samples-1)):
            vj=self.output[j]
            K1=-2*np.power(vj, 3)+3*np.power(vj, 2)
            a=vj+params.dt*K1
            K2=-2*np.power(a, 3)+3*np.power(a, 2)
            self.output[j+1]=vj+params.dt/2*(K1+K2)

          #  print "vj=", vj
          #  print "k1=", K1
          #  print "params.dt=", params.dt
          #  print "a=", a
          #  print "K2=", K2

class Model2(object):
    def __init__(self, params):
        print "Model 2 solving..."
        # model: v'=-2*v^3+3*v^2-w
        # w'=eps*(alpha*v-gamma-w)
        self.output = np.zeros((2,int(params.samples)))
        # initial condition
        self.output[0,0] = params.v0
        self.output[1, 0] = params.w0

        for j in range(0, int(params.samples - 1)):
            vj = self.output[0,j]
            wj = self.output[1, j]
            K1v = -2 * np.power(vj, 3) + 3 * np.power(vj, 2)-wj
            K1w = params.eps * (params.alpha*vj-params.gamma-wj)
            av = vj + params.dt * K1v
            aw = wj + params.dt * K1w
            K2v = -2 * np.power(av, 3) + 3 * np.power(av, 2)-aw  #??????
            K2w = params.eps * (params.alpha * av - params.gamma - aw)

            self.output[0, j + 1] = vj + params.dt / 2 * (K1v + K2v)
            self.output[1, j + 1] = wj + params.dt / 2 * (K1w + K2w)
        #print vj
        #print wj
       # print "converges to: ", (-2*np.power(vj,3)+ 3 * np.power(vj, 2)), "=", (params.alpha*vj-params.gamma)

