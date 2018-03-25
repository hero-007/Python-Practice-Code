from os import listdir
from os.path import isfile, join

mypath = r'C:\Users\HP\Desktop\J.A.R.V.I.S'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
