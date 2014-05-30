#steup file for py2exe
# use command :python setup.py py2exe 
# to generate the windows execute binary
#
from distutils.core import setup
import os
import py2exe


Mydata_files = []
#add software
currentdir=os.path.join(os.getcwd(),'software')
for files in os.listdir(currentdir):
	f1 =  os.path.join(currentdir,files)
	if os.path.isfile(f1): # skip directories
		f2 = 'software', [f1]
		Mydata_files.append(f2)
	else :# os.path.isdir(f1)
		directory=files
		for subfile in os.listdir(f1):
			subf=os.path.join(f1, subfile)
			f3= 'software/'+directory,[subf]
			Mydata_files.append(f3)
#add bundler camera and help
camera=os.path.join(os.getcwd(),'osmbundler/cameras/cameras.sqlite')
ff='osmbundler/cameras',[camera]
Mydata_files.append(ff)
helptxt=os.path.join(os.getcwd(),'osmbundler/help.txt')
ff='osmbundler',[helptxt]
Mydata_files.append(ff)

#add pmvs & cmvs
helptxt=os.path.join(os.getcwd(),'osmpmvs/help.txt')
ff='osmpmvs',[helptxt]
Mydata_files.append(ff)

helptxt=os.path.join(os.getcwd(),'osmcmvs/help.txt')
ff='osmcmvs',[helptxt]
Mydata_files.append(ff)

setup(
	console=['RunBundler.py','RunCMVS.py','RunPMVS.py'],
	data_files=Mydata_files,
	 
)