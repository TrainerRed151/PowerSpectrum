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

for i in range(ngal):
    x[i] = random.uniform(0, L);
    y[i] = random.uniform(0, L);
    z[i] = random.uniform(0, L);


#plt.plot(k, pktemp);
#plt.xscale('log');
#plt.yscale('log');
#plt.show();
