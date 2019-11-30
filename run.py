from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV
import dataAnalisys as ana
from sklearn.cluster import KMeans
import pandas as pd
import glob

years = []
for y in range(2000,2019):
    years.append(str(y))

#print(list(ana.makeCsvSet("C:/Users/LG/Desktop/world-development-indicators/Indicators2000IndicateUnique.csv",1,674)))
'''
ana.makeCsv("C:/Users/LG/Desktop/world-development-indicators/Indicators.csv","C:/Users/LG/Desktop/world-development-indicators/Indicators2000year.csv",4,years)
ana.makeCsvUnique("C:/Users/LG/Desktop/world-development-indicators/Indicators2000year.csv","C:/Users/LG/Desktop/world-development-indicators/Indicators2000IndicateUnique.csv",3)
ana.attrCsv(list(ana.makeCsvSet("C:/Users/LG/Desktop/world-development-indicators/Indicators2000IndicateUnique.csv",1,1)),[1,4],"C:/Users/LG/Desktop/world-development-indicators/Indicators2000year.csv","C:/Users/LG/Desktop/world-development-indicators/Indicators1344.csv",[3,5])

ana.makeCsv("C:/Users/LG/Desktop/world-development-indicators/Indicators2000year.csv","C:/Users/LG/Desktop/world-development-indicators/IndicatorsBrithRate.csv",3,["SP.DYN.CBRT.IN"])
'''
#find best parameters
'''
birthRate = pd.read_csv("C:/Users/LG/Desktop/world-development-indicators/IndicatorsBrithRate.csv")
rate = birthRate["Value"]

meta = pd.DataFrame(birthRate).values
rate = pd.Series(rate).values

scaler = MinMaxScaler()
rate = scaler.fit_transform(rate.reshape(-1,1))

Kmeans = KMeans()
grid_dic={'n_clusters':[2,3,4,5],'n_init':[10,15,20,25,30,35,40],'max_iter':[10,20,30,40,50,60,70,80]}

gsc = GridSearchCV(Kmeans,param_grid=grid_dic)

gsc = gsc.fit(rate)
print(gsc.best_params_)
'''

#clustering and labeling brithRate
'''
birthRate = pd.read_csv("C:/Users/LG/Desktop/world-development-indicators/IndicatorsBrithRate.csv")
rate = birthRate["Value"]

meta = pd.DataFrame(birthRate).values
rate = pd.Series(rate).values

scaler = MinMaxScaler()
rate = scaler.fit_transform(rate.reshape(-1,1))

Kmeans = KMeans(n_clusters = 3, n_init=25,max_iter=80)
Kmeans.fit(rate)

ana.makeLabeling("C:/Users/LG/Desktop/world-development-indicators/IndicatorsBrithRate.csv","C:/Users/LG/Desktop/world-development-indicators/IndicatorsBrithRateLabel.csv",Kmeans.labels_)
'''

# remove no birth rate columns data
'''
nanCount = ana.selectiveNanOut("C:/Users/LG/Desktop/world-development-indicators/Indicators1344.csv","C:/Users/LG/Desktop/world-development-indicators/Indicators1344-1.csv",["SP.DYN.CBRT.IN"])
print(nanCount)
'''
# devide contries
'''
birthLabel = pd.read_csv("C:/Users/LG/Desktop/world-development-indicators/IndicatorsBrithRateLabel.csv")
Label = birthLabel['label']
Label = pd.Series(Label).values
ana.deviedContry("C:/Users/LG/Desktop/world-development-indicators/Indicators1344-1.csv","C:/Users/LG/Desktop/world-development-indicators","Indicators1344-3-",Label,[0,1,2])
'''
# preprocessing remove to many nan data columns
'''
devide = glob.glob("C:/Users/LG/Desktop/world-development-indicators\/Indicators1344-3-*.csv")
count = 0
for path in devide:
 indicators1344_1 = pd.read_csv(path)
 pd.set_option('display.max_rows',10000)
 pd.set_option('display.max_columns',10000)
 s = ana.getColumns(path,2,"end")

 nans = pd.Series(indicators1344_1.isna().sum()).values

 drop_list = []
 for index in range(2,len(nans)):
   if(nans[index]>100):
       drop_list.append(s[index-2])
 ana.selectiveOut(path,"C:/Users/LG/Desktop/world-development-indicators/Indicators1344-3-"+str(count)+"-p.csv",drop_list)

 indicators1344_2 = pd.read_csv("C:/Users/LG/Desktop/world-development-indicators/Indicators1344-3-"+str(count)+"-p.csv")
 pd.set_option('display.max_rows',10000)
 pd.set_option('display.max_columns',10000)
 print(indicators1344_2.isna().sum())
 print(len(list(indicators1344_2.isna().sum())))
 count+=1
'''
