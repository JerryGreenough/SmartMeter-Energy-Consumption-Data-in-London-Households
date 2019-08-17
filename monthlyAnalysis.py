import pandas as pd


dfsfile = pd.read_csv("./fileList.csv")


from multiEventPlotter import *

fname = dfsfile[(dfsfile["month"]==1) & (dfsfile["year"]==2013)]["processed"].iloc[0]
df012013 = pd.read_csv(fname)

fname = dfsfile[(dfsfile["month"]==2) & (dfsfile["year"]==2013)]["processed"].iloc[0]
df022013 = pd.read_csv(fname)

fname = dfsfile[(dfsfile["month"]==3) & (dfsfile["year"]==2013)]["processed"].iloc[0]
df032013 = pd.read_csv(fname)

fname = dfsfile[(dfsfile["month"]==4) & (dfsfile["year"]==2013)]["processed"].iloc[0]
df042013 = pd.read_csv(fname)

fname = dfsfile[(dfsfile["month"]==5) & (dfsfile["year"]==2013)]["processed"].iloc[0]
df052013 = pd.read_csv(fname)

fname = dfsfile[(dfsfile["month"]==6) & (dfsfile["year"]==2013)]["processed"].iloc[0]
df062013 = pd.read_csv(fname)

fname = dfsfile[(dfsfile["month"]==7) & (dfsfile["year"]==2013)]["processed"].iloc[0]
df072013 = pd.read_csv(fname)

df012013_ave = df012013.groupby(["time"]).mean()
df012013_ave.reset_index(inplace = True)

df022013_ave = df022013.groupby(["time"]).mean()
df022013_ave.reset_index(inplace = True)

df032013_ave = df032013.groupby(["time"]).mean()
df032013_ave.reset_index(inplace = True)

df042013_ave = df042013.groupby(["time"]).mean()
df042013_ave.reset_index(inplace = True)

df052013_ave = df052013.groupby(["time"]).mean()
df052013_ave.reset_index(inplace = True)

df062013_ave = df062013.groupby(["time"]).mean()
df062013_ave.reset_index(inplace = True)

df072013_ave = df072013.groupby(["time"]).mean()
df072013_ave.reset_index(inplace = True)

labs = ["2013-01", "2013-02", "2013-03", "2013-04", "2013-05", "2013-06", "2013-07"]
dflist = [df012013_ave, df022013_ave, df032013_ave, df042013_ave, df052013_ave, df062013_ave, df072013_ave]
multiEventPlotter(dflist, "Average Monthly Energy Consumption", col = "mean", labels = labs)