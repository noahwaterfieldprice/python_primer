# Exercise 8.24
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt


N = 10000
flips = np.random.randint(2, size=N)

# scalar version
p_scalar = np.zeros(N)
for i in range(N):
    p_scalar[i] = np.sum(flips[:i + 1]) / float(i + 1)

# vectorised version
I = np.arange(1, N + 1, dtype=float)
q = np.cumsum(flips)
p_vec = q / I

print np.allclose(p_scalar, p_vec)

plt.plot(I, p_vec)
plt.xlabel('number of flips')
plt.ylabel('probability of heads')
plt.title('Simulated probability of heads as a function of no. of coin flips')
plt.xscale('log')
plt.show()
