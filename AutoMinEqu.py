# The script is used to automate process of write files for minimization and equilibration

"""
For each protein the index number may have to be slightly modified to match the actual positions.

"""

import os
import glob
import sys
import fileinput

###############################################################

##############################################################
def makePBS(filename):
	minPBSname = filename + '-minPBS'
	nvtPBSname = filename + '-nvtPBS'
	nptPBSname = filename + '-nptPBS'
	f1=open(minPBSname,'w')
	f2=open(nvtPBSname,'w')
	f3=open(nptPBSname,'w')
	
	minName = filename+"-min"
	f1.writelines('### Lines starting with "#$" are options for the SGE scheduling system\n')
	f1.writelines('#$ -S /bin/bash    # Set shell to run job\n')
	f1.writelines('#$ -q all.q        # Choose queue to run job in\n')
	f1.writelines('#$ -pe orte 20      # Request one processor from parallel env.\n')
	f1.writelines('#$ -cwd            # Run job from my current working directory\n')
	f1.writelines('\n')
	f1.writelines('export LD_LIBRARY_PATH=/opt/gridengine/lib/linux-x64:/opt/openmpi/lib:/opt/python/lib:/home/amoffet2/amber14_plumed/lib\n')
	f1.writelines('export AMBERHOME="/home/amoffet2/amber14_plumed"\n')
	f1.writelines('export PATH="${AMBERHOME}/bin:$PATH"\n')
	f1.writelines('\n')
	f1.writelines('cd /home/qchen39/model/KAI2c-copy\n')
	f1.writelines('mpirun -np 20 pmemd.MPI -O -i min.in -o ' + filename+ '.out -p ' + filename + '.prmtop -c ' + filename +'.crd -r '+ minName +'.rst')



	nvtName = filename+"-nvt"
	f2.writelines('### Use this script for GPU jobs\n')
	f2.writelines('### Lines starting with "#$" are options for the SGE scheduling system\n')
	f2.writelines('#$ -S /bin/bash    # Set shell to run job\n')
	f2.writelines('#$ -q all.q        # Choose queue to run job in\n')
	f2.writelines('#$ -pe cuda 1      # Request one processor from the CUDA parallel env.\n')
	f2.writelines('#$ -l slots_gpu=1  # Request one GPU per CPU requested\n')
	f2.writelines('#$ -cwd            # Run job from my current working directory\n')
	f2.writelines('\n')
	f2.writelines('module load cuda\n')
	f2.writelines('nvidia-smi\n')
	f2.writelines('export AMBERHOME="/home/amoffet2/amber14/"\n')
	f2.writelines('export PATH="/home/amoffet2/amber14/bin:$PATH"\n')
	f2.writelines('export LD_LIBRARY_PATH=/opt/gridengine/lib/linux-x64:/opt/openmpi/lib:/opt/python/lib:/usr/local/cuda/lib64:/home/amoffet2/amber14/lib:/usr/local/cuda/lib64\n')
	f2.writelines('export CUDA_HOME=/usr/local/cuda\n')
	f2.writelines('\n')
	f2.writelines('export CUDA_VISIBLE_DEVICES=$(cat $TMPDIR/cuda_device)\n')
	f2.writelines('\n')
	f2.writelines('cd /home/qchen39/model/KAI2c-copy\n')
	f2.writelines('mpirun -np 1 pmemd.cuda.MPI -O -i NVT.in -o '+ nvtName +'.out -p '+ filename +'.prmtop -c '+ minName + '.rst -r '+ nvtName +'.rst -ref ' + minName + '.rst')


	nptName = filename+"-npt"
	f3.writelines('### Use this script for GPU jobs\n')
	f3.writelines('### Lines starting with "#$" are options for the SGE scheduling system\n')
	f3.writelines('#$ -S /bin/bash    # Set shell to run job\n')
	f3.writelines('#$ -q all.q        # Choose queue to run job in\n')
	f3.writelines('#$ -pe cuda 1      # Request one processor from the CUDA parallel env.\n')
	f3.writelines('#$ -l slots_gpu=1  # Request one GPU per CPU requested\n')
	f3.writelines('#$ -cwd            # Run job from my current working directory\n')
	f3.writelines('\n')
	f3.writelines('module load cuda\n')
	f3.writelines('nvidia-smi\n')
	f3.writelines('export AMBERHOME="/home/amoffet2/amber14/"\n')
	f3.writelines('export PATH="/home/amoffet2/amber14/bin:$PATH"\n')
	f3.writelines('export LD_LIBRARY_PATH=/opt/gridengine/lib/linux-x64:/opt/openmpi/lib:/opt/python/lib:/usr/local/cuda/lib64:/home/amoffet2/amber14/lib:/usr/local/cuda/lib64\n')
	f3.writelines('export CUDA_HOME=/usr/local/cuda\n')
	f3.writelines('\n')
	f3.writelines('export CUDA_VISIBLE_DEVICES=$(cat $TMPDIR/cuda_device)\n')
	f3.writelines('\n')
	f3.writelines('cd /home/qchen39/model/KAI2c-copy\n')
	f3.writelines('mpirun -np 1 pmemd.cuda.MPI -O -i NPT.in -o '+ nptName +'.out -p '+ filename +'.prmtop -c '+ nvtName + '.rst -r '+ nptName +'.rst -ref ' + nvtName + '.rst')


	f1.close()
	f2.close()
	f3.close()

###############################################################
##read strList line by line

pdbList = open("strList", 'r')
pdbName = []
for line in pdbList:
	if line != "":
		line = line.strip()
		pdbName.append(line)
pdbList.close()

for index in range(len(pdbName)):
	makePBS(pdbName[index])
#apply function repRes(pdbName)
###############################################################

