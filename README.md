# Dissertation Project: Feature Extraction and Random Forest model from Physiological Data

## Overview
This repository contains the implementation of a data processing pipeline designed to extract statistical features from physiological datasets. The focus is on analyzing frailty through various physiological metrics, including heart rate (HR), heart rate variability (HRV), respiratory rate (RR), and accelerometer data.

## Technologies Used
- Python 3.x
- Libraries: NumPy, Pandas, SciPy, Plotly, Matplotlib, Scikit-learn

## Dataset
The dataset used in this project is composed of multiple CSV from real word evidence. Each file contains physiological signals collected from participants, elder people in real time.

## Directory Structure
. ├── Dataset/ │ └── Frail/ # Directory containing input CSV files ├── Features/ # Directory for saving extracted features ├── ecg_preprocess.py # Module for ECG preprocessing ├── br_resp_preprocess.py # Module for respiratory preprocessing ├── kalman_filter.py # Module for Kalman filtering ├── windows.py # Module for windowing signals ├── main.py # Main script for processing data └── README.md # This file
