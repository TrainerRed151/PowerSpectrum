#!/usr/bin/env python

# Copyright (c) 2017 Brian Pomerantz. All Rights Reserved.

import random;
import numpy as np;
import matplotlib.pyplot as plt;
import math;
import sys;

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

print(deltak);
print(np.fft.fftfreq(N, N/L));
print(kf);

#plt.plot(k, pktemp);
#plt.xscale('log');
#plt.yscale('log');
#plt.show();
