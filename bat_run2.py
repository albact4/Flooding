# -*- coding: utf-8 -*-
import tempfile
import subprocess
import os
from PyQt5.QtCore import QFileInfo  # Import QFileInfo if you're using PyQt

tmpdir = tempfile.mkdtemp(prefix='rf2qgis')
temp = os.path.join(tmpdir, "temp.bat")

dat_paths = [
    r"C:\Users\Rojano\Downloads\FinalVersion37\base\base",
]

with open(temp, "w") as f:
    f.write("C:\n")
    f.write('cd "C:\\Program Files\\Hydronia\\RiverFlow2D"\n')  # Use double backslashes
    for path in dat_paths:
        f.write(f'RiverFlow2dm5 "{path}" > "{QFileInfo(path).absolutePath()}/Run.log" \n')

subprocess.Popen(temp, shell=True)
