import nibabel as nib
filename = 'DET0000101_avg.nii'
img = nib.load(filename)
img.shape
#(512, 512, 539)
