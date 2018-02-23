#https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

#shape
print('shape: ', dataset.shape)

#head
print('\npeak\n', dataset.head(20))

# descriptions
print('\ndescriptions\n', dataset.describe())

# class distribution
print('\nclass distribution\n', dataset.groupby('class').size())

# #candles
# dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# plt.show()

# #histograms
# dataset.hist()
# plt.show()

# #scatter plot matrix
# scatter_matrix(dataset)
# plt.show()

#split-out validation dataset
array = dataset.values
# ... 5.1
