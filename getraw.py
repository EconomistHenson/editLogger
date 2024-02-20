# import city of Ottawa Covid Waste Water Data

# Jan 16 2024

import os, sys
import pandas as pd
from datetime import datetime


from multReps import multReps


# raw data to be processed
fname ='./2024Jan15/wastewater_virus.csv'
wWaterVirus = pd.read_csv(fname)
# load in Dataframe
wWaterVirusDF = pd.DataFrame(wWaterVirus)
varnames = wWaterVirusDF.columns
print(wWaterVirus.describe())
print(varnames)

ObsNo = wWaterVirusDF.count()


#setup dataframe to collect factoids

if(os.path.isfile('CovWaterStats.cvs')):
   CovWaterStats = pd.read_csv('CovWaterStats.cvs')
else:
   StatsColNames = ['SubMatter','PyProg','RunDat','Varname','VarVal'] 
   CovWaterStats = pd.DataFrame(columns=StatsColNames)
   print('line34 ************************')
   print(' creating new dataframe')
   print(CovWaterStats)
   print('line37 ************************')
# update date
TheDate = datetime.today().strftime('%Y,%m,%d')

# add the number of observations
ObsNo = wWaterVirus.shape[0]
# form dictionary of new record
anewrec = {'SubMatter':'SurveyOverView',
          'PyProg': 'getraw.py',
           'RunDat':TheDate ,
           'Varname':'ObsNo',
           'VarVal':ObsNo}
print('*****line 46')
print(anewrec)
print('****line 48')
print(StatsColNames)
pnewdf = pd.DataFrame(anewrec,index=[0])
print('*********************')
print('line 53 pnewrec=',pnewdf)
print('*****************')
CovWaterStats=pd.concat([CovWaterStats,pnewdf],ignore_index=True)
print('================================')
print(CovWaterStats)

#===============================
#
#  Analysis of Sample Dates
#
#===============================

print('*** line 61')
exec(open('samprng.py').read())

CovWaterStats.to_csv('CovWaterStats.csv')


