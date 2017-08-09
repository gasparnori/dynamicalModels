import matplotlib.pyplot as plt
import numpy as np

class Plotter(object):
    def __init__(self,  outp, parameters):
       # self.input=inp
        self.output=outp
        self.times= np.linspace(parameters.time_min, parameters.time_max, parameters.samples)
        self.plot()
    def plot(self):
        #input_plot=plt.plot(self.times, self.input, 'r', label='input')
        output_plot=plt.plot(self.output, 'b', label='output')
        #plt.legend(bbox_to_anchor=(1, 1))
        #plt.legend([input_plot, output_plot], ['input', 'output'])
        plt.show()
