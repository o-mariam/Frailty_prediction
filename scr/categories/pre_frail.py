import numpy as np
import pandas as pd

import os
from sklearn import preprocessing

from pathlib import Path


path = Path("C:\\Users\\Admin\\Ceid\\ΔΙΠΛΩΜΑΤΙΚΗ\\wwsx_matlab\\Dataset\\Pre-frail")

files = path.glob("*.csv")



for f in files:

    try:
        filepath = os.path.join(path, f)

        if os.path.isfile(f):
            with open(f, newline='') as csvfile:
                                        
                    features_z=pd.DataFrame(columns=['az_avg', 'az_std', 'az_p5', 'az_p95', 'az_mode_val', 'az_skew_val', 'az_kurt_val', 'az_energy', 'az_entropy_val'])
                    features_x=pd.DataFrame(columns=['ax_avg', 'ax_std', 'ax_p5', 'ax_p95', 'ax_mode_val', 'ax_skew_val', 'ax_kurt_val', 'ax_energy', 'ax_entropy_val'])
                    features_y=pd.DataFrame(columns=['ay_avg', 'ay_std', 'ay_p5', 'ay_p95', 'ay_mode_val', 'ay_skew_val', 'ay_kurt_val', 'ay_energy', 'ay_entropy_val'])
                    features_hr=pd.DataFrame(columns=['hr_avg', 'hr_std', 'hr_p5', 'hr_p95', 'hr_mode_val', 'hr_skew_val', 'hr_kurt_val', 'hr_energy', 'hr_entropy_val'])
                    features_hrv=pd.DataFrame(columns=['hrv_avg', 'hrv_std', 'hrv_p5', 'hrv_p95', 'hrv_mode_val', 'hrv_skew_val', 'hrv_kurt_val', 'hrv_energy', 'hrv_entropy_val'])
                    features_rr=pd.DataFrame(columns=['rr_avg', 'rr_std', 'rr_p5', 'rr_p95', 'rr_mode_val', 'rr_skew_val', 'rr_kurt_val', 'rr_energy', 'rr_entropy_val'])
                    features_br=pd.DataFrame(columns=['br_avg', 'br_std', 'br_p5', 'br_p95', 'br_mode_val', 'br_skew_val', 'br_kurt_val', 'br_energy', 'br_entropy_val'])
                    features_resp=pd.DataFrame(columns=['resp_avg', 'resp_std', 'resp_p5', 'resp_p95', 'resp_mode_val', 'resp_skew_val', 'resp_kurt_val', 'resp_energy', 'resp_entropy_val'])
                    label=pd.DataFrame(columns=['Y'])
                    Id=pd.DataFrame(columns=['part_id'])
                    
                    frail=pd.read_csv(csvfile,low_memory=False)



                    filename=str(f)
                    print(filename)
                    
                #     print(filename)
                    filename=filename.rsplit("\\")[-1]

                    hr=frail['ecg_hr']
                    out1= ecg_preprocess.d_wavelet(hr, 'sym5', 1)
                    hr_w= windows.split_into_windows(out1, 120)

                    for i,w in enumerate(hr_w):

                                part_id=frail['part_id'].iloc[0]
                                Id.loc[len(Id)] = pd.Series(part_id, index=Id.columns)


                        #    Create the array with the label of the patient

                                Y='Pre_frail'
                                label.loc[len(label)] = pd.Series(Y, index=label.columns)                                
                                feat_hr=f.extract_statistical_features(w)
                                features_hr.loc[len(features_hr)] = pd.Series(feat_hr, index=features_hr.columns)

                    print("features_hr")

                    print("ID")




                    hrvv=frail['ecg_hrv']
                    out2= ecg_preprocess.d_wavelet(hrvv, 'sym5', 1)
                    hrv_w= windows.split_into_windows(out2, 120)

                    for i,w in enumerate(hrv_w):


                        feat_hrv=f.extract_statistical_features(w)
                        features_hrv.loc[len(features_hrv)] = pd.Series(feat_hrv, index=features_hrv.columns)
                    print("feat_hrv")
                    rr=frail['ecg_rr']
                    out3= ecg_preprocess.d_wavelet(rr, 'sym5', 1)
                    rr_w= windows.split_into_windows(out3, 120)

                    for i,w in enumerate(rr_w):

                        feat_rr=f.extract_statistical_features(w)
                        features_rr.loc[len(features_rr)] = pd.Series(feat_rr, index=features_rr.columns)
                    print("feat_rr")

                    from scr.preprocessing import br_resp_preprocess, ecg_preprocess, kalman_filter, feature_extraction, \
                        windows

                    br=frail['br']
                    out4= br_resp_preprocess.d_wavelet(br, 'sym5', 1)
                    br_w= windows.split_into_windows(out4, 120)

                    for i,w in enumerate(br_w):


                        feat_br=f.extract_statistical_features(w)
                        features_br.loc[len(features_br)] = pd.Series(feat_br, index=features_br.columns)
                    print("feat_br")
                    resp=frail['resp_piezo']
                    out5= br_resp_preprocess.d_wavelet(resp, 'sym5', 1)
                    resp_w= windows.split_into_windows(out5, 120)

                    for i,w in enumerate(resp_w):

                        feat_resp=f.extract_statistical_features(w)
                        features_resp.loc[len(features_resp)] = pd.Series(feat_resp, index=features_resp.columns)

                    print("feat_resp")


                ########          For the accelerometer data

                    xa=frail['acc_x']

                    ## Split windows 

                    import scr.preprocessing.windows

                    xa_w= windows.split_into_windows(xa, 120)

                    for i,w in enumerate(xa_w):

                        ax=np.array(w)
                        ax=ax.reshape(-1,1)
                        kf = kalman_filter.KalmanFilter(q=0.001, r=0.1, dt=1 / 25)
                        filtered = kf.filter(ax)
                        filtered= kalman_filter.filter_but(filtered)


                        feat_acc=f.extract_statistical_features(filtered)
                        features_x.loc[len(features_x)] = pd.Series(feat_acc, index=features_x.columns)

                    print("x")


                    xa=frail['acc_y']

                    xa_w= windows.split_into_windows(xa, 120)
                    for i,w in enumerate(xa_w):

                        ax=np.array(w)
                        ax=ax.reshape(-1,1)
                        kf = kalman_filter.KalmanFilter(q=0.001, r=0.1, dt=1 / 25)
                        filtered = kf.filter(ax)
                        filtered= kalman_filter.filter_but(filtered)


                        feat_acc=f.extract_statistical_features(filtered)
                        features_y.loc[len(features_y)] = pd.Series(feat_acc, index=features_y.columns)

                    print("y")


                    xa=frail['acc_z']

                    xa_w= windows.split_into_windows(xa, 120)

                    for i,w in enumerate(xa_w):
     
                        ax=np.array(w)
                        ax=ax.reshape(-1,1)
                        kf = kalman_filter.KalmanFilter(q=0.001, r=0.1, dt=1 / 25)
                        filtered = kf.filter(ax)
                        filtered= kalman_filter.filter_but(filtered)


                        feat_acc=f.extract_statistical_features(filtered)
                        features_z.loc[len(features_z)] = pd.Series(feat_acc, index=features_z.columns)

                    print("z")


  

                    merged_df = pd.concat([Id,features_x, features_y, features_z,features_hr,features_hrv,features_rr,features_br,features_resp,label], axis=1)

                    merged_df.to_csv('C:\\Users\\Admin\\Ceid\\ΔΙΠΛΩΜΑΤΙΚΗ\\wwsx_matlab\\Features\\Pfrail\\' + filename)
                    
            directory = "C:\\Users\\Admin\\Ceid\\ΔΙΠΛΩΜΑΤΙΚΗ\\wwsx_matlab\\Dataset\\p"

            csvfile.close()

            os.remove(filepath)
            print(f"File {filename} deleted successfully.")


    except Exception as e:
            print(f"Error processing {f}: {e}")

                






















        # features_list=[ 'hr_avg', 'hr_std', 'hr_p5', 'hr_p95', 'hr_mode_val', 'hr_skew_val', 'hr_kurt_val', 'hr_energy', 'hr_entropy_val',
        #                 'hrv_avg', 'hrv_std', 'hrv_p5', 'hrv_p95', 'hrv_mode_val', 'hrv_skew_val', 'hrv_kurt_val', 'hrv_energy', 'hrv_entropy_val',
        #                 'rr_avg', 'rr_std', 'rr_p5', 'rr_p95', 'rr_mode_val', 'rr_skew_val', 'rr_kurt_val', 'rr_energy', 'rr_entropy_val',
        #                 'br_avg', 'br_std', 'br_p5', 'br_p95', 'br_mode_val', 'br_skew_val', 'br_kurt_val', 'br_energy', 'br_entropy_val',
        #                 'ba_avg', 'ba_std', 'ba_p5', 'ba_p95', 'ba_mode_val', 'ba_skew_val', 'ba_kurt_val', 'ba_energy', 'ba_entropy_val',
        #                 'resp_avg', 'resp_std', 'resp_p5', 'resp_p95', 'resp_mode_val', 'resp_skew_val', 'resp_kurt_val', 'resp_energy', 'resp_entropy_val',
        #                 'ax_avg', 'ax_std', 'ax_p5', 'ax_p95', 'ax_mode_val', 'ax_skew_val', 'ax_kurt_val', 'ax_energy', 'ax_entropy_val'
        #                 'ay_avg', 'ay_std', 'ay_p5', 'ay_p95', 'ay_mode_val', 'ay_skew_val', 'ay_kurt_val', 'ay_energy', 'ay_entropy_val',
        #                 'az_avg', 'az_std', 'az_p5', 'az_p95', 'az_mode_val', 'az_skew_val', 'az_kurt_val', 'az_energy', 'az_entropy_val']