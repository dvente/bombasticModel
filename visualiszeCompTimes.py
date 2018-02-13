import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['backend'] = "Qt4Agg"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('compTimes.log')

#mean and std comp time by opt level table 
data.dropna().groupby('optLevel').agg({'compTime':['mean','std'],'lenthOfSolution':['mean']}).to_latex()

data.plot()
