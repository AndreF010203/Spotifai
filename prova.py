# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

from numpy import *
from scipy import *

tracklist = genfromtxt('tracks_final.csv', skip_header=1, usecols=(0, 3), missing_values="nan", filling_values="0")

print(tracklist)