#!/usr/bin/env python

# Copyright (c) 2017 Brian Pomerantz. All Rights Reserved.

import random;
import sys;
import csv;

L = float(sys.argv[1]);
ngal = int(sys.argv[2]);

f = open('random.dat', 'w');
writer = csv.writer(f, lineterminator='\n');
for i in range(ngal):
    x = random.uniform(0, L);
    y = random.uniform(0, L);
    z = random.uniform(0, L);
    writer.writerow([x, y, z]);
