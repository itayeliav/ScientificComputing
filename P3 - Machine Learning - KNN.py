
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import math

dataset = pd.read_csv('files\\titanic_data.csv')

#Normalizing categorical variables
#Sex: Male=0, Female=1 | Embarked: S=0, C=1, Q=2
dataset['Sex']=dataset['Sex'].replace('male',0)
dataset['Sex']=dataset['Sex'].replace('female',1)
dataset['Embarked']=dataset['Embarked'].replace('S',0)
dataset['Embarked']=dataset['Embarked'].replace('C',1)
dataset['Embarked']=dataset['Embarked'].replace('Q',2)

#Replacing Null values to the mean values
#This is done in order to take those rows into account
mean = int(dataset['Age'].mean(skipna=True))
dataset['Age'] = dataset['Age'].replace(np.NaN, mean)
dataset['Embarked'] = dataset['Embarked'].replace(np.NaN, 0)


# Split Dataset
X = dataset.iloc[:,0:8]
y = dataset.iloc[:,8]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.2)

#Scaling the data
# Transforms all the values to be between -1 and 1 to keep the data standardized.
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)



#Choosing K
#math.sqrt(len(X_train)) = 26.68
#We prefer odd numbers to reduce ambiguity: 26.68 => 27
#Varying K manually - Best results for K=7

optimal_k=7


#Defining the model: Init KNN
classifier = KNeighborsClassifier(n_neighbors=optimal_k,p=2,metric='euclidean')

classifier.fit(X_train,y_train)


#Predict the test set resulets
y_pred = classifier.predict(X_test)

#Evaluate Model (Kept in code for future use)
cm = confusion_matrix(y_test,y_pred)

acc =round( accuracy_score(y_test,y_pred) * 100 , 2)

#Results:
print("Optimal K:{}, Best Accuracy: {}%".format(optimal_k,acc))

