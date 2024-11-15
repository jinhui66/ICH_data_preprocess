import os
import re
import SimpleITK as sitk
import random
from matplotlib import pyplot as plt
import torch
import pandas as pd
import copy

    
path = "/home/wangchangmiao/jinhui/DATA/ICH-DATA/raw_data/"
ct_path = "/home/wangchangmiao/jinhui/DATA/ICH-DATA/processed_data/"
good_path = path + "good/"
bad_path = path + "bad/"
good_ct_path = ct_path + "good/"
bad_ct_path = ct_path + "bad/"

content = []
file_info = []
pid = 0
for text in os.listdir(good_path):
    pid += 1
    if text != 'desktop.ini':
        path = good_ct_path + f"{pid}.nii.gz"
        ori_text = text.replace("  "," ")
        text = ori_text.split(' ')
        # print(text)
        if text[2][0] == 'M':
            gender = 1
        elif text[2][0] == 'F':
            gender = 0
            
        age = text[2][1:]
        outcome = 1
        if '手术' in text[8]:
            treatment_assignment = 1
        else:
            treatment_assignment = 0 

        GCS = text[6][3:-1]

        file_info.append({
            'Pid': pid,
            'treatment assignment': treatment_assignment,
            'outcome': outcome,
            'path': path,
            'gender': gender,
            'age': age,
            'GCS': GCS,
            'text': ori_text
        })
    # f.writelines(good+'#good'+'#\n')
pid = 0
for text in os.listdir(bad_path):
    # print("./data/raw_data/bad/" + text)
    pid += 1
    path = bad_ct_path + f"{pid}.nii.gz"
    if text != 'desktop.ini':
        ori_text = text.replace("  "," ")
        text = ori_text.split(' ')
        # print(text)
        if text[2][0] == 'M':
            gender = 1
        elif text[2][0] == 'F':
            gender = 0
            
        age = text[2][1:]

        outcome = 0
        if '手术' in text[8]:
            treatment_assignment = 1
        else:
            treatment_assignment = 0 

        GCS = text[6][3:-1]

        file_info.append({
            'Pid': pid,
            'treatment assignment': treatment_assignment,
            'outcome': outcome,
            'path': path,
            'gender': gender,
            'age': age,
            'GCS': GCS,
            'text': ori_text,
        })
# random.shuffle(file_info)
df = pd.DataFrame(file_info)
df.to_excel('./data/table.xls', index=False)
        

    
# def read_dicom(path):
#     reader = sitk.ImageSeriesReader()
#     dicom = reader.GetGDCMSeriesFileNames(path)
#     # print(dicom)
#     reader.SetFileNames(dicom)
#     image = reader.Execute()
#     img_array = sitk.GetArrayFromImage(image)
#     return image_array

# vision,a = read_dicom("good\zz\1.2.392.200036.9116.2.5.1.37.2418728709.1486790989.937543\1.2.392.200036.9116.2.5.1.37.2418728709.1486791091.373999")

