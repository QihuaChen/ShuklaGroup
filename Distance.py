import mdtraj as md
import glob
import numpy as np

ref_traj="firsttraj.pdb"
ref_helix_index = md.load(ref_traj).topology.select("resSeq 148 to 163") # T2
ref_helix = md.load(ref_traj).atom_slice(ref_helix_index)

x = open("T2x", 'w')
y = open("T1T3y", 'w')
z = open("T1T3-select", 'w')

T2Group = [148, 163]
T1T3Group = [136, 169]

count=0
framecount = 0
for file in glob.glob('5CBK-Apo-round*'):	
	traj = md.load(file, top="5CBK-stripped.prmtop")
	target = md.compute_contacts(traj, [T2Group, T1T3Group]) #y
	target1 = target[0]
	target1=np.asarray(target1, dtype=float)
	target2 = md.load(file, top="5CBK-stripped.prmtop").atom_slice(ref_helix_index)
	r = md.rmsd(target2, ref_helix)
	#np.save(file+"rmsd", r)
	
	for i in range(len(target1)):
		array = target1[i]
		x.write(str(r[i])+"\n")
		y.write(str(array[1])+"\n")
		if (array[1]<2.5):
			targetfile = file.replace("-stripped", "")
                        z.write(targetfile)
                        z.write(" ")
                        z.write(str((i+1))+"\n")



        count+=1
        print("I am at " +file+" finished: ", count)		
		

x.close()
y.close()
z.close()

with open("T1T3-select", "rb") as source:
        lines = [line for line in source]

random_choice = random.sample(lines, 50)

with open("randomSelect", "wb") as sink:
        sink.write(b"".join(random_choice))



