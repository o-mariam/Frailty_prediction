import numpy as np
from scipy.stats import skew, kurtosis, entropy
from scipy.stats import mode
import pandas as pd


from scipy.stats import entropy


import pyeeg.pyeeg as p

def approximate_entropy(signal):
    min_len = 16  # Minimum length required by ap_entropy
    if len(signal) < min_len:
        # Pad signal with zeros
        signal = np.concatenate([signal, np.zeros(min_len - len(signal))])
    return p.ap_entropy(signal, 2, 0.2*np.std(signal))

# def approximate_entropy(signal):
#     return p.ap_entropy(signal, 2, 0.2*np.std(signal))
def extract_statistical_features(data):
    
    features = []
    try:
        avg = np.mean(data)
        std = np.std(data)
        p5 = np.percentile(data, 5)
        p95 = np.percentile(data, 95)
        mode_val, _ = mode(data,keepdims=True)
        modee = mode_val[0] if mode_val.size != 0 else 0
        skew_val = skew(data)
        kurt_val = kurtosis(data)
        energy = np.sum(np.square(data))
        entropy_val = approximate_entropy(data)
        features.extend([avg, std, p5, p95, modee, skew_val, kurt_val, energy, entropy_val])
    except TypeError as e:
        print("TypeError occurred:", e)
    except ValueError as e:
        print("ValueError occurred:", e)
    except ZeroDivisionError as e:
        print("ZeroDivisionError occurred:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
    return features
