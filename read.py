import nibabel as nib
import torch
import matplotlib.pyplot as plt
import SimpleITK as sitk

# 加载.nii.gz文件
filename = 'nii_data/bad/109.nii.gz'
img = sitk.ReadImage(filename)
 
# 获取图像数据
data = sitk.GetArrayFromImage(img) 
print(len(data))
L = len(data)

plt.imshow(data[L//2,:,:], cmap='gray')
plt.show()
# for z in range(L):
#     plt.imshow(data[z,:,:], cmap='gray')
#     plt.show()