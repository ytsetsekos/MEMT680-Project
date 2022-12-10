# -*- coding: utf-8 -*-
"""
MEM T680 Project - Yanni Tsetsekos
For more on TLE's: https://en.wikipedia.org/wiki/Two-line_element_set
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
# from pathlib import Path

from cesium import featurize
    
# from beyond.io.tle import Tle
# from beyond.dates import Date, timedelta

# def readTLEdata(filename):
    # Takes in TLE data as txt file and records data over all lines

TLE_count = 0 # starts at 0 for first TLE
# preallocating arrays for length of the landsat data set:
inclination = np.zeros((5990,1)) # orbital inclination (degrees)
epoch_year = np.zeros((5990,1)) # last two digits of year, starting in 1999
mean_motion = np.zeros((5990,1)) # (the first derivative of mean motion), angular speed across sky to complete 1 orbit
mean_motion_rev = np.zeros((5990,1)) # number of orbits completed each day (revolutions per day)
right_ascension = np.zeros((5990,1)) # orbital position parameter
TLE_num = np.zeros((5990,1)) # TLE set number (unique number for each TLE)

with open('landsat7.txt', 'r') as f: # reading in data from landsat7 historical TLE data.
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].strip().split() # stripping line to elements
        if i%2==0: # this is a first line of a TLE
            epoch_year[TLE_count] = int(line[3][0:2])
            mean_motion[TLE_count] = float(line[4]) 
            # add more paramaters here, for TLE 1st line: 
        if i%2==1: # then this is the second line
            inclination[TLE_count] = float(line[2])
            right_ascension[TLE_count] = float(line[3])
            mean_motion_rev[TLE_count] = float(line[7])
            # add more paramaters here, for TLE 2nd line:
            
            TLE_count = TLE_count +1 # iterate TLE ind
            
    # plt.plot(epoch_year, inclination)
    # plt.plot(inclination)
    # plt.plot(mean_motion_rev)
    plt.plot(right_ascension)
    
    
# Featurization: 

features_to_use = ["amplitude",
                   "percent_beyond_1_std",
                   "maximum",
                   "max_slope",
                   "median",
                   "median_absolute_deviation",
                   "percent_close_to_median",
                   "minimum",
                   "std",
                   "weighted_average"]
# Creating features just for inclination data to start
features_inclination = featurize.featurize_time_series(times=TLE_count,
                                              values=inclination,
                                              errors=None,
                                              features_to_use=features_to_use)
print(features_inclination)
# preds_cesium = model_cesium.predict(features_inclination)
print('Done')