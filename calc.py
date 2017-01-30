#!/usr/bin/env python

# Copyright (c) 2017 Brian Pomerantz. All Rights Reserved.

import random;
import numpy as np;
import matplotlib.pyplot as plt;
import math;
import sys;

def mag(a, b, c):
    return math.sqrt(a*a + b*b + c*c);

if len(sys.argv) != 4:
    print('Invalid number of arguments');
    exit();

L = float(sys.argv[1]);
N = int(sys.argv[2]);
ngal = int(sys.argv[3]);

x = np.zeros(ngal);
y = np.zeros(ngal);
z = np.zeros(ngal);

n = np.zeros((N, N, N));
deltax = -1*np.ones((N, N, N), dtype=float);

nbar = float(ngal)/(N*N*N);
kf = 2.0*math.pi/L;

# NGP Method
for i in range(ngal):
    x[i] = random.uniform(0, L);
    y[i] = random.uniform(0, L);
    z[i] = random.uniform(0, L);
    
    xi = int(round((N-1)*x[i]/L));
    yi = int(round((N-1)*y[i]/L));
    zi = int(round((N-1)*z[i]/L));

    n[xi][yi][zi] += 1;
    deltax[xi][yi][zi] += 1.0/nbar;

deltak = abs(np.fft.fftn(deltax, (N, N, N)))**2;

#print(deltak);
#print(np.fft.fftfreq(N, N/L));
#print(kf);

ktemp = np.fft.fftfreq(N, N/L);

kmag = np.arange(kf, kf*N/2.0, kf);
pk = np.zeros(len(kmag));

# Average to find monopole moment
sum = 0.0;
for l in range(len(kmag)):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                d = mag(ktemp[i], ktemp[j], ktemp[k]);
                if d > (kmag[l] - kf/2.0) and d < (kmag[l] + kf/2.0):
                    pk[l] += deltak[i][j][k];
                    sum += 1.0;
    pk[l] = pk[l]/sum;

pk = L**3*pk/N**6.0;

print(kmag);
print(pk);

#plt.plot(kmag, pk);
#plt.xscale('log');
#plt.yscale('log');
#plt.show();
