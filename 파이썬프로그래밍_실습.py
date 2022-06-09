#plt.title("이준혁")

import numpy as np
import matplotlib.pyplot as plt

data_file = np.genfromtxt("c:\\pythontest\\data_file.txt",delimiter=',')
#print(data_file.shape)
#print(data_file[0:2,:])

time = data_file[:,0]
time = time - time[0]

sensors = data_file[:,1:5]

#print(sensors.shape)
#print(sensors[0:3])

avg = np.mean(sensors,1) # over the 2nd dimension

#print(avg[0:3])

my_data = np.hstack((time.reshape(1200,1),sensors,avg.reshape(1200,1)))

np.savetxt('c:\\pythontest\\data.txt',(1200 , 9),delimiter=',')

plt.plot(time/60.0, sensors[:, 1], 'ro', label = "Sensor 2")
plt.plot(time/60.0, sensors[:, 2], 'gx', label = "Sensor 3")
plt.plot(time/60.0, avg, 'b.', label = "Average Sensors 1-4")

plt.legend()
plt.xlabel('Time (min)')
plt.ylabel('Sensor Values')
plt.savefig('c:\\pythontest\\202210962_이준혁.pdf')
plt.title("202210962_LeeJunHyuk")
plt.show()

