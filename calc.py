#!/usr/bin/env python

# Copyright (c) 2017 Brian Pomerantz. All Rights Reserved.

import numpy as np;
#import matplotlib.pyplot as plt;
import math;
import sys;
import csv;

def mag(a, b, c):
    return math.sqrt(a*a + b*b + c*c);

def fileLen(fname):
    with open(fname, 'r') as f:
        return int(f.readline());

if len(sys.argv) != 4:
    print('Invalid number of arguments');
    exit();

L = float(sys.argv[1]);
N = int(sys.argv[2]);
file = sys.argv[3];
#ngal = int(sys.argv[3]);
ngal = fileLen(file);

x = np.zeros(ngal);
y = np.zeros(ngal);
z = np.zeros(ngal);

#n = np.zeros((N, N, N));
deltax = -1*np.ones((N, N, N), dtype=float);

nbar = float(ngal)/((N-1)**3);
kf = 2.0*math.pi/L;
kN = math.pi*N/L;

f = open(file, 'rt');
reader = csv.reader(f, delimiter=' ');
i = -1;
for row in reader:
    if (i != -1):
        x[i] = float(row[1]);
        y[i] = float(row[2]);
        z[i] = float(row[3]);
    i += 1;

# NGP Method
for i in range(ngal):
    xi = int(round((N-1)*x[i]/L));
    yi = int(round((N-1)*y[i]/L));
    zi = int(round((N-1)*z[i]/L));

    #n[xi][yi][zi] += 1;
    deltax[xi][yi][zi] += 1.0/nbar;

deltak = np.fft.fftn(deltax, (N, N, N));
fac = 0.5*math.pi/kN;

for i in range(N):
    for j in range(N):
        for k in range(N):
            deltak[i][j][k] *= np.sinc(fac*i)*np.sinc(fac*j)*np.sinc(fac*k);

deltak = abs(deltak)**2;

ktemp = 2.0*math.pi*np.fft.fftfreq(N, d=L/N);

kmag = np.arange(kf, 0.5*kf*N, kf);
pk = np.zeros(len(kmag));

# Average to find monopole moment
for l in range(len(kmag)):
    sum = 0.0;
    for i in range(int((N+1)/2)):
        for j in range(int((N+1)/2)):
            for k in range(int((N+1)/2)):
                d = mag(ktemp[i], ktemp[j], ktemp[k]);
                if d > (kmag[l] - 0.5*kf) and d < (kmag[l] + 0.5*kf):
                    pk[l] += deltak[i][j][k];
                    sum += 1.0;
    if sum != 0:
        pk[l] = pk[l]/sum;

pk = (L**3.0)*pk/((N-1)**6.0);

# Plot power spectrum
#pdfplot = plt.figure();
#plt.plot(kmag, pk);
#plt.xscale('log');
#plt.yscale('log');
#plt.xlabel('k');
#plt.ylabel('P(k)');
#plt.show();
#pdfplot.savefig('test.pdf');


# Output values to file
f2 = open('pk.dat', 'w');
writer = csv.writer(f2, lineterminator='\n');
for i in range(len(kmag)):
    writer.writerow([kmag[i], pk[i]]);
