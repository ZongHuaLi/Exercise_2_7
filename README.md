# Exercise 2.7: Data-Driven SISO-OFDM Channel Estimation

This project implements a ...

## Project Overview
- **Objective**: This project aims to implement and evaluate channel estimation techniques for a SISO-OFDM system. We compare two approaches: a **DNN-based estimator** (using a multi-layer perceptron) and a **Linear Minimum Mean Square Error (LMMSE) estimator**.
- **Performance Evaluation**: The system is evaluated based on Mean Square Error (MSE) performance across various Signal-to-Noise Ratios (SNR) ranging from 5 dB to 40 dB. We also demonstrate the impact of inter-symbol interference (ISI) by comparing scenarios with and without a Cyclic Prefix (CP).


## Environment Setup (Windows/RTX 4050)
The project is configured for Windows 10/11 with an NVIDIA RTX 4050 GPU for hardware acceleration:
1. **Create the virtual environment with the specific Python version:**
    ```bash
    conda create -n tensorflow python=3.9.19 -y

2. **Activate the environment:**
    ```bash
    conda activate tensorflow

3. **Install CUDA Toolkit via Conda:**
    ```bash
    conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0

4. **Install all required packages via requirements.txt:**
   ```bash
   pip install -r requirements.txt

## Implementation Details & Modifications
To complete this exercise, I performed the following technical implementations:
1. **DNN-based Estimator Implementation:**
    Completed the # YOUR CODE HERE blocks in tools/networks.py using TensorFlow 1.x.
    Defined the input placeholders and constructed a multi-layer perceptron architecture with ReLU activation and MSE loss optimization.

2. **LMMSE Estimator Implementation:**
    Manually implemented the MMSE_CE function in tools/raputil.py.
    Derived and calculated the channel autocovariance matrix (RHH) assuming a uniform power delay profile to derive the optimal LMMSE weight matrix (WMMSE).


## Dataset Download
The data set cannot be uploaded to GitHub due to its large file size. It can be downloaded from the following Google Drive link:
[download dataset](https://drive.google.com/drive/folders/1RfGs-HHSjNnYyosmEFZe8z7iAQ9fPnav?usp=sharing)

Next, place `channel_train.npy` and `channel_test.npy` in the path: `./tools`

## Execution Workflow

| Checklist | Configuration |
|-----------|---------------|
| **Train DNN** | Set ce_type = 'dnn', test_ce = False in main.py. |
| **Evaluate DNN** | Set ce_type = 'dnn', test_ce = True in main.py. |
| **Evaluate LMMSE** | Set ce_type = 'mmse', test_ce = True in main.py. |
| **Remove CP** | Toggle CP_flag = False in main.py to observe performance degradation due to ISI. |
| **Run** | Execute: `python main.py` for each configuration phase. |
   