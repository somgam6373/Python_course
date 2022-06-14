'''
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
'''

# Pandas => 데이터를 테이블 형태로 다룬다.
# DataFrame: 데이터 테이블 전체 객체
# Series: 각 열 데이터를 다루는 개체

# 한글이 있으면 한글과 관련된 인코딩을 해야만함

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_file = pd.read_csv('c:\\pythontest\\data_with_headers.csv')

time = data_file['time']
time = time - time[0]

sensors = data_file.loc[:,'s1': 's4']
avg_row = np.mean(sensors,1)
avg_col = np.mean(sensors, 0)

result = pd.concat([time, sensors, avg_row], axis =1)
result.to_csv('c:\\pythontest\\result.csv')
#result.to_excel('c:\\pythontest\\result.xlsx')
result.to_html('c:\\pythontest\\result.htm')

plt.plot(time, sensors['s1'], 'r-', label = 'Sensor 2')
plt.plot(time, avg_row, 'b', label = 'Average')

plt.xlabel('Time (sec)')
plt.ylabel('Sensor Values')
plt.legend()
plt.title('202210962_LeeJunHyuk')
plt.savefig('c:\\pythontest\\my_Python_plot.png')




















'''흰_눈_아래
환희_웃던
그대_모습_보고싶어라

따뜻한_눈꽃에
향기만이_가득하네

사계절_맴돈
짙은_암향
매화_아닌_제비였으니

이별과_작별_사이
그_무언가
슬픔이여_안녕
슬픔이여_안녕'''