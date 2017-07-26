import mdtraj as md
from msmbuilder.featurizer import DihedralFeaturizer
import numpy as np
import glob

featurizer='DihedralFeaturizer'
path='/home/qchen39/Apo/stripped'
topology='/home/qchen39/Apo/5CBK-stripped.prmtop'
traj_format='mdcrd'

for file in glob.glob(path+'/*.'+traj_format):
	t=md.load(file,top=topology)
	ftr=DihedralFeaturizer(types=['phi','psi','chi1'])
	f=ftr.transform(t)
	traj=file.split('/')[-1].split('.')[0]
	outfile=path+'/'+featurizer+'_'+traj+'.npy'
	np.save(outfile,f)
