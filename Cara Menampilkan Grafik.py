# Cara Menampilkan Grafik

import matplotlib.pyplot as plt
from numpy import arange,sin,cos

x = arange(0.0,6.0,0.1)
plt.plot(x,sin(x),'o-',x,cos(x),'x-')
plt.title('Grafik Sinusoidal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend('sinus','cosinus',loc=0)
plt.grid(True)
plt.show()
