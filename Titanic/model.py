import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

x_train = train_data.get(['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])
y_train = train_data.get(['Survived'])

has_family = x_

train_data.head()