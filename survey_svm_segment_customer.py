import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import zipfile
import os
import glob
import numpy as np
from scipy import stats
import tensorflow as tf
from sklearn.cluster import KMeans as Kmeans
from kmodes.kmodes import KModes
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

print(os.getcwd())
os.chdir("/home/sewoong/Desktop/thinking-design")
csv_li = glob.glob("*.csv")
print(csv_li)
k = input()
survey = pd.read_csv(csv_li[int(k)])


#survey1 = pd.read_csv(csv_li[-2])
#survey = pd.concat([survey, survey1], axis = 0)
#print(survey.columns)
#print(survey.head())
#print(len(survey.index))

survey = survey.iloc[:,1:]

for col in survey.columns :
	survey[col] = survey[col].astype("category")
	if any(survey[col].isnull()):
		#print(survey[col].cat.categories.tolist())
		#input()
		survey[col] = survey[col].fillna(survey[col].cat.categories.tolist()[0])
		#survey[col].fillna(0)
		#print(survey.isnull())

#print(survey.columns)
#print(survey.iloc[:,2])
#survey_code = pd.DataFrame(survey.shape)
#survey_code.index = pd.CategoricalIndex(survey)

#print(pd.CategoricalIndex(survey))
#print(survey.columns)
#print(survey.head())
#print(survey)

#create model and prediction
'''
model = Kmeans(n_clusters = 3, algorithm = 'auto')
model.fit(survey)
predict = pd.DataFrame(model.predict(survey))
predict.columns = ['predict']

#concatenate labels to df as a new col
survey_ = pd.concat([survey, predict], axis= 1)

plt.scatter(survey_.iloc[4], survey_.iloc[5], c = survey_['predict'], alpha =0.5)


centers = pd.DataFrame(model.cluster_centers_,columns=[survey.columns[4],survey.columns[5]])
center_x = centers[survey.columns[4]]
center_y = centers[survey.columns[5]]
plt.scatter(center_x,center_y,s=50,marker='D',c='r')
plt.show()
'''

km = KModes(n_clusters = 4, init = 'Huang', n_init = 10, verbose = True)
clusters = km.fit_predict(survey)
#print('cccccc',km.cluster_centroids_)

predict = pd.DataFrame(clusters)
predict.columns = ['predict']
#print(predict)

survey_ = pd.concat([survey, predict], axis= 1)

#print(survey_.head())

#category to integer
survey_int = survey.copy()
for i in survey.columns :
	survey_int[i] = survey[i].cat.codes

survey_int = pd.concat([survey_int, predict], axis = 1)

pdclu = pd.DataFrame(km.cluster_centroids_, columns = survey.columns)

survey_vi = pd.concat([survey, pdclu], axis = 0)

for i in survey_vi.columns:
	survey_vi[i] = survey_vi[i].astype("category")

survey_vi_int = survey_vi.copy()
for i in survey_vi.columns:
	survey_vi_int[i] = survey_vi[i].cat.codes

centers = survey_vi_int.iloc[-3:]
'''
#category to onehot vec
survey_onehot = survey.copy()
for i in survey.columns:
	survey_onehot = pd.get_dummies(survey_onehot, columns = [i], prefix = [i])
'''
#print(survey.columns)
#print(len(survey_int.iloc[:,4]), len(survey_int.iloc[:,5]), len(survey_int.iloc[:,-1]))
#print(survey_int.iloc[:,4:6])

'''
plt.scatter(survey_int.iloc[10], survey_int.iloc[12], c = survey_int.iloc[-1], alpha =0.5)
print(predict['predict'])
'''

print(len(survey_int.iloc[:,4]), len(survey_int.iloc[:,9]), len(survey_int.iloc[:,-1]))
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(survey_int.iloc[:,4], survey_int.iloc[:,9], survey_int.iloc[:,17], c = survey_int.iloc[:,-1], s = 70, alpha = 0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

#predict to csv file


'''
center_x = centers[survey_vi_int.columns[4]]
center_y = centers[survey_vi_int.columns[5]]

print(len(center_x))

plt.scatter(center_x,center_y,s=50,marker='D',c='r')
'''
plt.show()

#predict.to_csv('survey_seg.csv')
print(km.cluster_centroids_)