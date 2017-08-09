import matplotlib.pyplot as plt
import matplotlib.artist
import matplotlib.legend
import numpy as np
import general_params
import cell
import stimulation

p=general_params.Params()
i=stimulation.stim(p.samples, "sine")
neuron=cell.Cell(0, i.stim_current)


fig=plt.figure(2)
fig.canvas.set_window_title('Hogdkin-Huxley model')
plt.subplot(2, 1, 1)
times=np.linspace(0, p.time_max, num=p.samples)
plt.plot(times, neuron.V, 'b', label='Vm')
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
