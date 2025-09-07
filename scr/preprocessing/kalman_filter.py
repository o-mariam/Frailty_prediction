import pandas as pd
import matplotlib.pyplot as plt

from sklearn import preprocessing
from math import log10, sqrt


import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import butter, lfilter
import warnings
from scipy.optimize import OptimizeWarning
from scipy.signal import butter, filtfilt

warnings.simplefilter("ignore", category=OptimizeWarning)


import numpy as np


def setup_kalman(q, r, dt):
    A = np.array([[1, dt], [0, 1]])
    H = np.array([[1, 0]])
    P = np.zeros((2, 2))
    x = np.zeros((2, 1))
    return A, H, P, x

def p(A, x, P, q):
    x = np.dot(A, x)
    P = np.dot(np.dot(A, P), A.T) + q
    return x, P

def u(x, P, H, r, z):
    y = z - np.dot(H, x)
    S = np.dot(np.dot(H, P), H.T) + r
    K = np.dot(np.dot(P, H.T), np.linalg.inv(S))
    x = x + np.dot(K, y)
    P = np.dot((np.eye(2) - np.dot(K, H)), P)
    return x, P

def KalmanFilter(data, q, r, dt):
    A, H, P, x = setup_kalman(q, r, dt)
    filtered_data = []
    for measurement in data:
        x, P = p(A, x, P, q)
        x, P = u(x, P, H, r, measurement)
        filtered_data.append(x[0])
    return np.array(filtered_data)

# Sample rate:
sample_rate = 25
time_step = 1 / sample_rate




def filter_but(output):
    

    fs=25
    cutoff_freq = 0.3 # Hz

    nyquist_freq = 0.5 * fs
    normal_cutoff = cutoff_freq / nyquist_freq
    b, a = butter(4, normal_cutoff, btype='high', analog=False)

    out = filtfilt(b, a, output)

    

    return out



