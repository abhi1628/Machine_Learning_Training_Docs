
# How do I make my pandas DataFrame smaller and faster?
import pandas as pd
data = pd.read_csv('http://bit.ly/kaggletrain')
data.head()

pd.get_dummies(data.Sex).iloc[:, 1:]
# How do I create dummy variables in pandas?
