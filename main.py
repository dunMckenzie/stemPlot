import matplotlib.pyplot as plt
import numpy as np

n = np.arange(0, 32)
x = np.cos((np.pi * n))

period = 8

plt.stem(n, x, linefmt = 'grey' , markerfmt = '*')
plt.title('Stem Plot of x[n] = cos((pi*n)/4)')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()

#Verify periodicity with period N = 8
is_periodic = np.allclose(x[:period], x[-period:])
print(f"x[n] is periodic with period N = {period}: {is_periodic}")