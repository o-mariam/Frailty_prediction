
from tkinter import NONE
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pywt as pw
import matplotlib.pyplot as plt
import matplotlib.pyplot

from math import sqrt
import statistics
import math
from statsmodels import robust
from math import log10, sqrt
from sklearn import preprocessing

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

import numpy as np


def d_wavelet(signal,wavelet_family,noise_sigma):

  
        w = pw.Wavelet(wavelet_family) # Use Daubechies8 wavelet 
        # maxlev = pw.dwt_max_level(len(signal), w.dec_len)
        maxlev=10


       
        print("maximum level is " + str(maxlev))


        coeffs = pw.wavedec(signal,w, level=maxlev)
        
        s3=statistics.median(abs(coeffs[3]))/0.6745
        s4=statistics.median(abs(coeffs[4]))/0.6745
        s2=statistics.median(abs(coeffs[2]))/0.6745

        threshold2=s2*math.sqrt(2*np.log10(len(coeffs[2])))          
        threshold3=s3*math.sqrt(2*np.log10(len(coeffs[3])))          
        threshold4=s4*math.sqrt(2*np.log10(len(coeffs[4])))

        coeffs[2] = pw.threshold(coeffs[2], threshold2,mode='soft') # Filter the noise , mode=soft
        coeffs[3] = pw.threshold(coeffs[3], threshold3,mode='soft') 
        coeffs[4] = pw.threshold(coeffs[4], threshold4,mode='soft') 

#### Baseline Wander
        coeffs[0]=np.zeros(len(coeffs[0]))
        coeffs[1]=np.zeros(len(coeffs[1]))

  
        datarec = pw.waverec(coeffs,wavelet_family)
       
        return datarec

