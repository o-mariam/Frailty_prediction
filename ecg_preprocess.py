
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
         # Wavelet decomposition of the signal
         

        ### Display of coefficients
        # cA10,cD10,cD9,cD8,cD7,cD6,cD5,cD4,cD3,cD2,cD1=coeffs
        # fig,(ax11,ax10,ax9,ax8,ax7,ax6,ax5,ax4,ax3,ax2,ax1)= plt.subplots(11)


        # ax1.plot(cD1)
        # plt.title('cD1')

        # ax2.plot(cD2)
        # plt.title('cD2')

        # ax3.plot(cD3)
        # plt.title('cD3')

        # ax4.plot(cD4)
        # plt.title('cD4')

        # ax5.plot(cD5)
        # plt.title('cD5')

        # ax6.plot(cD6)
        # plt.title('cD6')

        # ax7.plot(cD7)
        # plt.title('cD7')

        # ax8.plot(cD8)
        # plt.title('cD8')

        # ax9.plot(cD9)
        # plt.title('cD9')

        # ax10.plot(cD10)
        # plt.title('cD10')

        # ax11.plot(cA10)
        # plt.title('cA11')


        # plt.show()


        s3=statistics.median(abs(coeffs[3]))/0.6745
        s4=statistics.median(abs(coeffs[4]))/0.6745
        s2=statistics.median(abs(coeffs[2]))/0.6745

        threshold2=s2*math.sqrt(2*np.log10(len(coeffs[2])))          
        threshold3=s3*math.sqrt(2*np.log10(len(coeffs[3])))          
        threshold4=s4*math.sqrt(2*np.log10(len(coeffs[4])))

        coeffs[2] = pw.threshold(coeffs[2], threshold2,mode='soft') # Filter the noise , mode=soft
        coeffs[3] = pw.threshold(coeffs[3], threshold3,mode='soft') 
        coeffs[4] = pw.threshold(coeffs[4], threshold4,mode='soft') 

        coeffs[0]=np.zeros(len(coeffs[0]))
        coeffs[1]=np.zeros(len(coeffs[1]))

  
        datarec = pw.waverec(coeffs,wavelet_family)
       
        return datarec

