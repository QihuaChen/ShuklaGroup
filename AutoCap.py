# The script is used to automate process of protein capping

"""
For each protein the index number may have to be slightly modified to match the actual positions.

"""

import os
import glob
import sys
import fileinput
###############################################################
# Generate a pdbList as the list of all structures
# eg. Shc1.B9999xxx without '.pdb' for wider usage


STRLIST = open("oldStrList", 'w')
STRLIST2 = open("strList", 'w')
pdb_files = glob.glob("Shc1.B9999*")

# ----- file name should be changed everytime

for f in pdb_files:
	f = f.replace(".pdb", "")
	STRLIST.write(f+"\n")
	STRLIST2.write("new"+f+"\n")
STRLIST.close()
STRLIST2.close()
###############################################################

def repRes(fileName):
	f=open(fileName,"r")
	newName = fileName.replace(".pdb","")
	f1=open('new'+fileName,'w')
#np.save('helix_RMSD'+ref_traj+'.npy',dataset)
	data=f.readlines()
	new_data=[]
	for index in range(len(data)):
		
		if  (index!= 7) and (index!= 9) and (index!= 2051) and (index!= 2052) and (index!= 2053) and (index!= 2054):
			if (index == 8) or (index == 10) or (index == 11):
					data[index] = data[index].replace("ALA","ACE")
					data[index] = data[index].replace("CA ","CH3")
			if (index == 2049) or (index == 2050):
					data[index] = data[index].replace("ALA","NME")
					data[index] = data[index].replace("CA ","CH3")
			if (index == 2055):
					data[index] = 'TER\n'
			new_data.append(data[index])
	
	f1.writelines(new_data)

	f.close()
	f1.close()

###############################################################
##read strList line by line

pdbList = open("oldStrList", 'r')
pdbName = []
for line in pdbList:
	if line != "":
		line = line.strip()
		pdbName.append(line+'.pdb')
pdbList.close()

for index in range(len(pdbName)):
	repRes(pdbName[index])
#apply function repRes(pdbName)
###############################################################

