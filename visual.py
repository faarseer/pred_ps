#from pyecharts import Bar
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import zipfile
import os
import glob
import numpy as np
from scipy import stats

print(os.getcwd())

print(glob.glob("*Data.csv"))
csv_list = glob.glob("*Data.csv")
#read csv file


pop = pd.read_csv(csv_list[1])

#print(pop.columns)
#print(pop.head())

#graph gender / ages axis 
pop.set_index("Country Code", inplace = True)
pop_CHN = pop.loc['CHN']
pop_KOR = pop.loc['KOR']

#print(pop_CHN["Series Name"])
#print(pop_CHN["Series Code"])
#print(pop_CHN.columns)

attr = []
for i in range(16):
	attr.append("{} - {}".format(5*i, 5*i + 4))

year = range(2009,2018)

pop_CHN_f = pop_CHN.iloc[3:19, 3:].astype(float)
pop_CHN_m = pop_CHN.iloc[20:36, 3:].astype(float)

pop_KOR_f = pop_KOR.iloc[3:19, 3:].astype(float)
pop_KOR_m = pop_KOR.iloc[20:36, 3:].astype(float)

'''
print(pop_CHN_f.head())
print(pop_CHN_f.columns)
print(pop_CHN_m.iloc[:,9])
print(pop_CHN_m['2009 [YR2009]'])
print(len(pop_CHN_f.columns), len(pop_CHN_f.columns))
'''

plt.style.use("ggplot")

fig, axes = plt.subplots(5,2)
fig.tight_layout()
for i in range(10):
	y = list(pop_CHN_f.iloc[:,i].T)
	y_ = list(pop_CHN_m.iloc[:,i].T) 
	xlabel = attr
	df = pd.DataFrame({'male': y_, 'female':y}, index = xlabel)
	df.plot.barh(ax = axes[i // 2,i % 2], yticks = np.arange(16), title = 'CHN_population in {}'.format(i+2009))

#plt.show()
#plt.savefig('./CHN_pop.pdf')

fig, axes = plt.subplots(5,2)
fig.tight_layout()
for i in range(10):
	#y = list(pop_CHN_f.iloc[:,i].T)
	y_ = list(pop_CHN_m.iloc[:,i].T) 
	xlabel = attr
	df = pd.DataFrame({'male': y_}, index = xlabel)
	df.plot.barh(ax = axes[i // 2,i % 2], yticks = np.arange(16), title = 'CHN_population in {}'.format(i+2009), color = 'blue')

	
fig, axes = plt.subplots(5,2)
fig.tight_layout()
for i in range(10):
	y = list(pop_KOR_f.iloc[:,i].T)
	y_ = list(pop_KOR_m.iloc[:,i].T)
	xlabel = attr
	df = pd.DataFrame({'male': y_, 'female':y}, index = xlabel)
	df.plot.barh(ax = axes[i // 2,i % 2], yticks = np.arange(16), title = 'KOR_population in {}'.format(i+2009))

#plt.show()
#plt.savefig('./KOR_pop.pdf')

fig, axes = plt.subplots(5,2)
fig.tight_layout()
for i in range(10):
	#y = list(pop_KOR_f.iloc[:,i].T)
	y_ = list(pop_KOR_m.iloc[:,i].T)
	xlabel = attr
	df = pd.DataFrame({'male': y_}, index = xlabel)
	df.plot.barh(ax = axes[i // 2,i % 2], yticks = np.arange(16), title = 'KOR_population in {}'.format(i+2009), color = 'blue')


pval = []
for i in range(10):
	pop_CHN_t = np.array(pop_CHN_f.iloc[:,i].T) +np.array(pop_CHN_m.iloc[:,i].T)
	pop_KOR_t = np.array(pop_KOR_f.iloc[:,i].T) +np.array(pop_KOR_m.iloc[:,i].T)
	pval.append(stats.ttest_ind(pop_CHN_t, pop_KOR_t, equal_var = False)[-1])

print(pval)


fig, axes = plt.subplots(5,2)
fig.tight_layout()
for i in range(10):
	y = list(pop_KOR_f.iloc[:,i].T)
	y_ = list(pop_KOR_m.iloc[:,i].T)
	pop_CHN_t = np.array(pop_CHN_f.iloc[:,i]) + np.array(pop_CHN_m.iloc[:,i])
	CHN_np = (pop_CHN_t - np.mean(pop_CHN_t, axis=0)) / np.std(pop_CHN_t, axis=0)
	pop_KOR_t = np.array(pop_KOR_f.iloc[:,i]) + np.array(pop_KOR_m.iloc[:,i])
	KOR_np = (pop_KOR_t - np.mean(pop_KOR_t, axis=0)) / np.std(pop_KOR_t, axis=0)
	df = pd.DataFrame(np.array([CHN_np,KOR_np]).T, columns = ['CHN_T','KOR_T'])
	df.boxplot(column = ['CHN_T','KOR_T'], ax = axes[i // 2,i % 2])

fig, axes = plt.subplots(5,2)
fig.tight_layout()
for i in range(10):
	y = list(pop_KOR_f.iloc[:,i].T)
	y_ = list(pop_KOR_m.iloc[:,i].T)
	pop_CHN_f = np.array(pop_CHN_f.iloc[:,i])
	CHN_np = (pop_CHN_f - np.mean(pop_CHN_f, axis=0)) / np.std(pop_CHN_f, axis=0)
	pop_KOR_f = np.array(pop_KOR_f.iloc[:,i]) 
	KOR_np = (pop_KOR_f - np.mean(pop_KOR_f, axis=0)) / np.std(pop_KOR_f, axis=0)
	df = pd.DataFrame(np.array([CHN_np,KOR_np]).T, columns = ['CHN_f','KOR_f'])
	df.boxplot(column = ['CHN_f','KOR_f'], ax = axes[i // 2,i % 2])

'''
fig, axes = plt.subplots(5,2)
fig.tight_layout()
for i in range(10):
	#y = list(pop_KOR_f.iloc[:,i].T)
	#y_ = list(pop_KOR_m.iloc[:,i].T)
	pop_CHN_f = np.array(pop_CHN_m.iloc[:,i])
	CHN_np = (pop_CHN_m - np.mean(pop_CHN_m, axis=0)) / np.std(pop_CHN_m, axis=0)
	pop_KOR_f = np.array(pop_KOR_m.iloc[:,i]) 
	KOR_np = (pop_KOR_m - np.mean(pop_KOR_m, axis=0)) / np.std(pop_KOR_m, axis=0)
	df = pd.DataFrame(np.array([CHN_np,KOR_np]).T, columns = ['CHN_m','KOR_m'])
	df.boxplot(column = ['CHN_m','KOR_m'], ax = axes[i // 2,i % 2])
'''


plt.show()
'''
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
y = list(pop_CHN_f.iloc[:,0].T)
y_ = list(pop_CHN_m.iloc[:,0].T)
xlabel = attr
df = pd.DataFrame({'male': y_, 'female':y}, index = xlabel)
df.plot.barh(ax = ax1)
'''

#a1.barh(x, y, width = 0.25, label = 'female')
#a1.barh(x + 0.25,y_, width = 0.25, color = 'g', label = 'male')
#plt.xticks(x, xlabel)
#plt.yticks(sorted(y))
#a1.bar(x + width, y, width, color=list(plt.rcParams['axes.prop_cycle'])[2]['color'])



'''
for l in y:
	chn_fe = []
	for i in attr:
		chn_fe.append([])
		ind = filter(lambda x: i in x, pop_CHN["Series Code"])
		ind_ = filter(lambda x: l in x, pop_CHN.columns)
		chn_fe[-1].append(pop_CHN[ind,ind_])
'''



