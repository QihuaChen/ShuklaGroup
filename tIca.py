import numpy as np
import glob
import msmbuilder.cluster
from msmbuilder.utils import io
from msmbuilder.decomposition import tICA

list1=[]
allstr=[]
for i in sorted(glob.glob('Dihedral*')):
	allstr.append(i)
	print(i)
	a = np.load(i)
	a1 = []
	for k in range(len(a)):
		a1.append(a[k][0])
	a1 = np.array(a1)
	list1.append(a1)

print(len(list1))
tica = tICA(n_components=5, lag_time=1)
tica.fit(list1)
tica_traj = tica.transform(list1)
np.save('tica_Apo', tica_traj)

'''
states = msmbuilder.cluster.KMeans(n_clusters=200)
states.fit(tica_traj)
io.dump(states,'clusters.pkl')
'''




######################
#to access the clustering data
#import pickle
#c= pickle.load(open('clusters.pkl','rb'))
#c.labels_
#c.n_clusters
#from msmbuilder.utils import io
#clusters = msmbuilder.cluster.KMeans(n_clusters=200)
#dataset = np.load('tica_Apo.npy')
#clusters.fit(dataset)
######################




'''
centers=states.cluster_centers_
l=states.labels_
n_cluster = states.n_clusters
n_traj=len(tica_traj)
n_frames=len(tica_traj)
count_matrix = np.zeros(n_cluster)
for j in range(0, n_traj):  
     for m in range(0,len(tica_traj[j])):
         cluster_id = l[j][m]
         count_matrix[cluster_id] = count_matrix[cluster_id]+1

sorted_array = count_matrix.argsort() #to sort the array from low to high and gives an array of index
take = np.zeros(10)
for n in range(10):
	take[n] = sorted_array[n]

strlist = open('leastDensityStrList','wb')
for o in range(10):
     for j in range(0, n_traj):
         for m in range(0,len(tica_traj[j])):
         	if(l[j][m] == take[o]):
         		name = allstr[j].split('_')[1].split('.')[0]
         		strlist. write(name)
         		trlist.write(" ")
         		strlist.write(str(m)+'\n')         
'''
