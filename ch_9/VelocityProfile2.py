# Exercise 9.7
# Author: Noah Waterfield Price


class VelocityProfile:

    def __init__(self, beta, mu0, n, R):
        self.beta, self.mu0, self.n, self.R = beta, mu0, n, R

    def value(self, r):
        beta, mu0, n, R = self.beta, self.mu0, self.n, self.R
        n = float(n)  # ensure float divisions
        v = (beta / (2.0 * mu0)) ** (1 / n) * (n / (n + 1)) *\
            (R ** (1 + 1 / n) - r ** (1 + 1 / n))
        return v


class VelocityProfile2(VelocityProfile):

    def __init__(self, beta, mu0, R):
        VelocityProfile.__init__(self, beta, mu0, None, R)

    def __call__(self, r, n):
        self.n = n
        return VelocityProfile.value(self, r)

# Evaluate v for various n values at r=0
v = VelocityProfile2(beta=0.06, mu0=0.02, R=2)
for n in 0.1, 0.2, 1:
    print v(0, n)


"""
Sample run:
python VelocityProfile2.py
10736.1818182
81.0
3.0
"""
