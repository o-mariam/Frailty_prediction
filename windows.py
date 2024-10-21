import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




def split_into_windows(array, window_size=2 * 60):

    
    samples_per_window = int(window_size * 25)
    windows_list = []

    # loop over all the rows of the dataframe
    for i in range(0, len(array), samples_per_window):
        window = array[i:i + samples_per_window]

        windows_list.append(window)

    # return the list of windows
    return windows_list