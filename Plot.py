from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

font = {'family':'Helvetica', 'size': 16}
plt.rc('font', **font)

#plt.rc('text', usetex=True)
#plt.rcParams['text.latex.preamble'] = [r'\boldmath']

T2axis=[]
T1T3axis=[]
f=open('T2x','rb')
#f=open('loop_RMSD'+ref_traj+'.npy','rb')
for line in f:
	T2axis.append(float(line))
f.close()
k=open('T1T3y','rb')
#f=open('helix_RMSD'+ref_traj+'.npy','rb')
for line in k:
	T1T3axis.append(float(line))
k.close()

#helixtMD=np.array(h)
#looptMD=np.array(l)

#loop=np.load('loop_RMSD'+ref_traj+'.npy')
#helix=np.load('helix_RMSD'+ref_traj+'.npy')
plt.hexbin(T2axis,T1T3axis, mincnt=1)
#plt.plot(T2axis,T1T3axis,'o')
#########
#plt.scatter(helixtMD, looptMD,color='magenta',s=10,alpha=0.8)

#plt.axis([0, 10, 0, 5])
plt.xlabel('T2 distance ($\AA$)',fontweight='bold')
plt.ylabel('T1-T3 distance ($\AA$)',fontweight='bold')

#plt.xticks(np.arange(0, 10, 2))
#plt.yticks(np.arange(0, 4, 0.5))
plt.show()
