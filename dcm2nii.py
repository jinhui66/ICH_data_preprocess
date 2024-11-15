import numpy as np
import shutil
import os
import SimpleITK as sitk

def dcm2nii_sitk(path_read, path_save, pid):
    reader = sitk.ImageSeriesReader()
    seriesIDs = reader.GetGDCMSeriesIDs(path_read)
    N = len(seriesIDs)
    lens = np.zeros([N])
    for i in range(N):
        dicom_names = reader.GetGDCMSeriesFileNames(path_read, seriesIDs[i])
        lens[i] = len(dicom_names)
    N_MAX = np.argmax(lens)
    dicom_names = reader.GetGDCMSeriesFileNames(path_read, seriesIDs[N_MAX])
    reader.SetFileNames(dicom_names)
    image = reader.Execute()
    sitk.WriteImage(image, path_save+ f'/{pid}.nii.gz')

rootpath = "./raw_data/bad"
Resultpath = './nii_data/bad'
patients = os.listdir(rootpath)
pid = 0
for patient in patients:
    path1 = rootpath + '/' + patient
    bs = os.listdir(path1)
    if len(bs) == 1:
        for b in bs:
            path2 = path1 + '/' + b
            cs = os.listdir(path2)
            if len(cs) == 1:
                for c in cs:
                    path3 = path2 + '/' + c
                    DICOMpath = path3
                    pid += 1
                    dcm2nii_sitk(DICOMpath , Resultpath, pid)
            else:
                DICOMpath = path2
                pid += 1
                dcm2nii_sitk(DICOMpath , Resultpath, pid) 



# # 重命名
# patients = os.listdir(rootpath)
# for patient in patients:
#     path1 = rootpath + '/' + patient
#     bs = os.listdir(path1)
#     if len(bs) == 1:
#         for b in bs:
#             path2 = path1 + '/' + b
#             cs = os.listdir(path2)
#             if len(cs) == 1:
#                 for c in cs:
#                     print(c)
#                     old_path = path2 + '/' + c
#                     new_path = path2 + '/1' 
#                     os.rename(old_path,new_path)
