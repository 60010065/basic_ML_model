import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

def mean(input_val):
    mean_value = sum(input_val)/len(input_val) 
    return mean_value

def start_plot():
    X = np.random.normal(0,1.8,[180,2])
    X[60:120] += 8
    X[120:,0] += 16
    plt.gca(aspect=1)
    plt.scatter(X[:,0],X[:,1])
    # plt.show()
    return X

def find_distance(a,b):
    distance = np.sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2)
    return distance
    

def set_new_centriod(data,center,epoch):
    for l in range(epoch):
        last_center = center
        cluster_group= []
        for i in range(len(data)):
            distance_list = []
            for j in range(len(center)):
                d = find_distance(data[i],center[j])
                distance_list.append(d)
            min_distance = np.argmin(distance_list)
            cluster_group.append(min_distance)
        reorderd_list = reordering(data,cluster_group,len(center))
        new_position = []
        
        reorderd_arr = np.array(reorderd_list)
        # print(reorderd_arr)
  
        for i in reorderd_arr:
            total_x = []
            total_y = []
            for j in range(len((i))):
                total_x.append(i[j][0])
                total_y.append(i[j][1])
            
            new_coordinate_x = mean(total_x)
            new_coordinate_y = mean(total_y)
            newpos = (new_coordinate_x,new_coordinate_y)
            new_position.append(newpos)
        center=np.asarray(new_position)
        print(l)    
        print('last_center',last_center)
        print('new_position',center)

        if (last_center == center).all():
            return center
        
    return center

        
def reordering(data,cluster,k_group):
    ordered_data = []
    for i in range(k_group):
        cluster_groups = []
        ordered_data.append(cluster_groups)
    for j in range(len(cluster)):
        for k in range(k_group):
            cluster_groups = []
            if cluster[j] == k:
                ordered_data[k].append(data[j])
                break
    return ordered_data
      

# np.random.seed(26)

k_centroid = 3


test_value = np.random.normal(0,1.8,[1,2])

X =start_plot()


init_value  = np.random.choice(len(X),k_centroid,replace=False)
init_centroid = X[init_value] # จุดเซนทรอยด์ตั้งต้น เลือกแบบสุ่ม

epoch = 50
new_center = set_new_centriod(X,init_centroid,epoch)
plt.figure
plt.gca(aspect=1)
plt.scatter(X[:,0],X[:,1])
plt.scatter(new_center[:,0],new_center[:,1],color='red')
plt.show()


