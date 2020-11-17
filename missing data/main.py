import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dữ liệu
dataset = pd.read_csv('train.csv')
dataset.info()
total = dataset.isnull().sum().sort_values(ascending=False)
print("total :",total)
percent = (dataset.isnull().sum()/dataset.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])

#Thể hiện 3 cột bị thiếu dữ liệu
#print(missing_data.head(3))


#Vẽ hình bằng code bên dưới

'''
f, ax = plt.subplots(figsize=(15, 6))
plt.xticks(rotation='90')
sns.barplot(x=missing_data.index, y=missing_data['Percent'])
plt.xlabel('Features', fontsize=15)
plt.ylabel('Percent of missing values', fontsize=15)
plt.title('Percent missing data by feature', fontsize=15)
plt.show()
'''

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
train = pd.read_csv("train.csv")
data = train[['Pclass', 'SibSp', 'Parch', 'Fare', 'Age']]
x_train = data[data['Age'].notnull()].drop(colums='Age')
y_train = data[data['Age'].notnull()]['Age']
x_test = data[data['Age'].isnull()].drop(colums = 'Age')
linreg.fit(x_train, y_train)
predicted = linreg.predict(x_test)
train.Age[train.Age.isnull()] = prediced
train.info()
