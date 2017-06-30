import mdtraj as md
import glob
import numpy as np

ref_traj="3W06.pdb"

ref_helix1 = md.load(ref_traj).topology.select("resSeq 151 to 163") # T2
ref_helix2 = md.load(ref_traj).topology.select("resSeq 168 to 181") # T3

ref_helix_index=np.concatenate((ref_helix1,ref_helix2),axis=0)

ref_helix = md.load(ref_traj).atom_slice(ref_helix_index)

dataset=[]

f=open('RMSD_tMDhelix.dat','wb')

for file in glob.glob('Shd1.B999*'):
      	target = md.load(file).atom_slice(ref_helix_index)
#target  mdtraj.compute_contact
      	r = md.rmsd(target, ref_helix)
	dataset.append(r)
#	i=0
#     	for i in range(0,len(r)):
#     		f.write(str(r[i]*10)+'\n')
#		f.write(str(r[i])+'\n')

np.save('helix_RMSD'+ref_traj+'.npy',dataset)
#print(dataset)
f.close()


dataset=[]
#np.save('helix_RMSD'+ref_traj+'.npy',dataset)
ref_loop_index = md.load(ref_traj).topology.select("resSeq 216 to 222")

ref_loop = md.load(ref_traj).atom_slice(ref_loop_index)

f=open('RMSD_tMDloop.dat','wb')

for file in glob.glob('Shd1.B999*'):
      	target = md.load(file).atom_slice(ref_loop_index)
      	r = md.rmsd(target, ref_loop)
	dataset.append(r)
#      	i=0
#     	for i in range(0,len(r)):
#     		f.write(str(r[i]*10)+'\n')
#		f.write(str(r[i])+'\n')
np.save('loop_RMSD'+ref_traj+'.npy',dataset)
#print(dataset)
f.close()



from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

font = {'family':'Helvetica', 'size': 20}
plt.rc('font', **font)

#plt.rc('text', usetex=True)
#plt.rcParams['text.latex.preamble'] = [r'\boldmath']

h=[]
l=[]
f=open('RMSD_tMDloop.dat','rb')
#f=open('loop_RMSD'+ref_traj+'.npy','rb')
for line in f:
       	l.append(float(line))
f.close()
f=open('RMSD_tMDhelix.dat','rb')
#f=open('helix_RMSD'+ref_traj+'.npy','rb')
for line in f:
       	h.append(float(line))
f.close()

helixtMD=np.array(h)
looptMD=np.array(l)

#h=[]
#l=[]
#f=open('RMSD_loop.dat','rb')
#for line in f:
#       	l.append(float(line))
#f.close()
#f=open('RMSD_helix.dat','rb')
#for line in f:
#       	h.append(float(line))
#f.close()

#helix=np.array(h)
#loop=np.array(l)

#plt.hexbin(helix, loop, bins=100, norm=LogNorm(), gridsize=100)
#plt.colorbar()
#########3
loop=np.load('loop_RMSD'+ref_traj+'.npy')
helix=np.load('helix_RMSD'+ref_traj+'.npy')
plt.plot(helix,loop,'o')
#########
plt.scatter(helixtMD, looptMD,color='magenta',s=10,alpha=0.8)

plt.axis([0, 10, 0, 5])
plt.xlabel('Helix rmsd ($\AA$)',fontweight='bold')
plt.ylabel('Loop rmsd ($\AA$)',fontweight='bold')

plt.xticks(np.arange(0, 10, 2))
plt.yticks(np.arange(0, 4, 0.5))
plt.show()
