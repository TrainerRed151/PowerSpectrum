#!/usr/bin/env python

# Copyright (c) 2017 Brian Pomerantz. All Rights Reserved.

import random;
import numpy as np;
#import matplotlib.pyplot as plt;
import math;
import sys;
import csv;

def mag(a, b, c):
    return math.sqrt(a*a + b*b + c*c);

def fileLen(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass;
    return i + 1;

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

nbar = float(ngal)/(N*N*N);
#kf = 2.0*math.pi/L;
kf = 1.0/L;

f = open(file, 'rt');
reader = csv.reader(f);
i = 0;
for row in reader:
    x[i] = float(row[0]);
    y[i] = float(row[1]);
    z[i] = float(row[2]);
    i += 1;

# NGP Method
for i in range(ngal):
    #x[i] = random.uniform(0, L);
    #y[i] = random.uniform(0, L);
    #z[i] = random.uniform(0, L);
    
    xi = int(round((N-1)*x[i]/L));
    yi = int(round((N-1)*y[i]/L));
    zi = int(round((N-1)*z[i]/L));

    #n[xi][yi][zi] += 1;
    deltax[xi][yi][zi] += 1.0/nbar;

deltak = abs(np.fft.fftn(deltax, (N, N, N)))**2;

#print(deltak);
#print(np.fft.fftfreq(N, d=L/N));
#print(kf);

ktemp = np.fft.fftfreq(N, d=L/N);

kmag = np.arange(0, 0.5*kf*N, kf);
pk = np.zeros(len(kmag));

# Average to find monopole moment
for l in range(len(kmag)):
    sum = 0.0;
    for i in range(int((N+1)/2)):
        for j in range(int((N+1)/2)):
            for k in range(int((N+1)/2)):
                d = mag(ktemp[i], ktemp[j], ktemp[k]);
                if d > (kmag[l] - kf/2.0) and d < (kmag[l] + kf/2.0):
                    pk[l] += deltak[i][j][k];
                    sum += 1.0;
    if sum != 0:
        pk[l] = pk[l]/sum;

pk = (L**3.0)*pk/(N**6.0);

#print(kmag);
#print(pk);

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
