import wheel.bdist_wheel
import zipfile
import os

whl_file = 'c:\\Users\\cmotte\\WheelUnpack\\numpy-1.26.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl'
target_dir = 'c:\\Users\\cmotte\\WheelUnpack\\unpacked'

with zipfile.ZipFile(whl_file, 'r') as zip_ref:
    zip_ref.extractall(target_dir)

print(f'Unpacked {whl_file} to {target_dir}')
