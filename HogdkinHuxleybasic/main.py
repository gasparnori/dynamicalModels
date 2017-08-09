import params
import numpy as np
import HodgkinHuxley
import matplotlib.pyplot as plt
import matplotlib.artist
import matplotlib.legend
import input
#import plotter
import solver



p=params.Params()
i=input.Input(p, "sine")

#m=solver.Model1(p)
#fig=plt.figure(1)
#fig.canvas.set_window_title('Model1')

#output_plot = plt.plot(m.output, 'b', label='output')
#plt.legend([output_plot], ['output'])
#plt.show()


#m2=solver.Model2(p)
#fig=plt.figure(2)
#fig.canvas.set_window_title('Model2')
#output_plot = plt.plot(m2.output[0,:], 'b', label='output')
#output_plot = plt.plot(m2.output[1,:], 'r', label='output')
#plt.show()

m3=HodgkinHuxley.HoHu(p, i.stim_current)
fig=plt.figure(2)
fig.canvas.set_window_title('Hogdkin-Huxley model')
plt.subplot(2, 1, 1)
times=np.linspace(0, p.time_max, num=p.samples)
plt.plot(times, m3.V, 'b', label='Vm')
plt.title('Membrane potential')
plt.ylabel('Vm [mV]')
plt.xlabel('[msec]')

plt.subplot(2, 1, 2)
plt.title('Stimulation')
plt.plot(times, i.stim_current, 'b', label='I0')
plt.ylabel('I0 [uA]')
plt.xlabel('[msec]')
plt.show()
exit()