# Frailty prediction for the elderly

## Overview
This repository contains the implementation of a data processing pipeline designed to extract statistical features from physiological datasets. The combined dataset, which consists of real data collected from older individuals, is used to train a Random Forest model, which is one of the models applied in this analysis. Additionally, we explore another model based on the method described in the paper [Tensor Decomposition for Multiple-Instance Classification of High-Order Medical Data](https://onlinelibrary.wiley.com/doi/full/10.1155/2018/8651930). The focus is on analyzing frailty through various physiological metrics, including heart rate (HR), heart rate variability (HRV), respiratory rate (RR), and accelerometer data.



## Technologies Used
- Python 3.x
- Libraries: NumPy, Pandas, SciPy, Plotly, Matplotlib, Scikit-learn

## Dataset
The dataset used in this project is composed of multiple CSV files. Each file contains physiological signals collected from older participants.

## Data Processing Workflow
The script processes each CSV file in the Dataset/Frail directory as follows:

Load the data using Pandas.
Preprocess physiological signals:
- Heart Signals: Discrete Wavelet Transform (DWT) is applied to denoise the heart rate (HR) and heart rate variability (HRV) signals.
- Accelerometer Data: Kalman filtering and a Butterworth filter are used to denoise the accelerometer data (X, Y, and Z axes).

Extract statistical features for various physiological metrics (e.g., HR, HRV, RR, accelerometer data).
Save the extracted features into a new CSV file in the Features directory.

## Directory Structure
. ├── Dataset/ │ └── Frail/ # Directory containing input CSV files ├── Features/ # Directory for saving extracted features ├── ecg_preprocess.py # Module for ECG preprocessing ├── br_resp_preprocess.py # Module for respiratory preprocessing ├── kalman_filter.py # Module for Kalman filtering ├── windows.py # Module for windowing signals ├── main.py # Main script for processing data └── README.md # This file

## Usage
-To run the main processing script, execute the following command in your terminal:
    python main.py

## License
This project is licensed under the MIT License - see the LICENSE file for details.
