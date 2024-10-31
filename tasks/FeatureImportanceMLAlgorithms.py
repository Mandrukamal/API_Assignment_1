import pandas as pd
import numpy as np
 
df = pd.read_csv("/Users/mkmac/Documents/API_assignment_1/data/ImputedStudentPerformanceFactors.csv")
print(df)

from sklearn import preprocessing
import matplotlib.pyplot as plt

# Encode the Categorical data of Gender - using Dummy Column - Creates a new column called Gender_M
# Use Dummy Variables
df = pd.get_dummies(df, columns=['Gender'], drop_first=True)

print(df.columns)
print(df.columns[0])
X = df.iloc[:,[0,1,4,5,7,10]]
Y = df.iloc[:,[6]]

# 1. Decision Tree
# Decision tree algorithms like classification and regression trees (CART) offer importance scores based on the reduction in the criterion used to select split points, like Gini or entropy.
# After being fit, the model provides a feature_importances_ property that can be accessed to retrieve the relative importance scores for each input feature.
from sklearn.tree import DecisionTreeClassifier
# define the model
model = DecisionTreeClassifier()
# fit the model
model.fit(X,Y)
# get importance
importance = model.feature_importances_
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
plt.bar([x for x in range(len(importance))], importance)

# 2. Random Forest Feature Importance
# After being fit, the model provides a feature_importances_ property that can be accessed to retrieve the relative importance scores for each input feature.
from sklearn.ensemble import RandomForestRegressor
# define the model
model = RandomForestRegressor()
# fit the model
model.fit(X,Y)
# get importance
importance = model.feature_importances_
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
plt.bar([x for x in range(len(importance))], importance)

# 3. Permutation Feature Importance - using KNN
from sklearn.neighbors import KNeighborsClassifier
from sklearn.inspection import permutation_importance

# define the model
model = KNeighborsClassifier()
# fit the model
model.fit(X,Y)
# perform permutation importance
results = permutation_importance(model, X, Y, scoring='accuracy')
# get importance
importance = results.importances_mean
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
plt.bar([x for x in range(len(importance))], importance)