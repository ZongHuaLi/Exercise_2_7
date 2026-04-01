import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import os


snr_range =[5, 10, 15, 20, 25, 30, 35, 40]

files_info = {
    'DNN (with CP)':    ('MSE_dnn_4QAM.mat',           'MSE_dnn_4QAM',           'b-o'),
    'DNN (without CP)': ('MSE_dnn_4QAM_CP_FREE.mat',   'MSE_dnn_4QAM_CP_FREE',   'b--^'),
    'LMMSE (with CP)':    ('MSE_mmse_4QAM.mat',          'MSE_mmse_4QAM',          'r-s'),
    'LMMSE (without CP)': ('MSE_mmse_4QAM_CP_FREE.mat',  'MSE_mmse_4QAM_CP_FREE',  'r--d')
}

plt.figure(figsize=(9, 6))

for label, (filename, key, style) in files_info.items():
    if os.path.exists(filename):
        mat_data = sio.loadmat(filename)
        
        mse_linear = np.array(mat_data[key]).flatten()
        
        mse_db = 10 * np.log10(mse_linear)
        
        plt.plot(snr_range, mse_db, style, label=label, linewidth=2, markersize=8)
    else:
        print(f"No file: {filename}")

plt.title('MSE vs. SNR for SISO-OFDM Channel Estimation', fontsize=15, fontweight='bold')
plt.xlabel('SNR (dB)', fontsize=13)
plt.ylabel('MSE (dB)', fontsize=13)

plt.xticks(snr_range)
plt.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)

plt.legend(fontsize=12)

plt.savefig('MSEvsSNR_Result.png', dpi=300, bbox_inches='tight')

plt.show()